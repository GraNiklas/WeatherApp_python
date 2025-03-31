import requests
from xml.etree import ElementTree
from datetime import datetime
import os

namespaces = {
    "wfs": "http://www.opengis.net/wfs/2.0",
    "BsWfs": "http://xml.fmi.fi/schema/wfs/2.0",
}


url = 'https://opendata.fmi.fi/wfs?service=WFS&version=2.0.0&request=getFeature&storedquery_id=fmi::observations::weather::simple&place=Helsinki&parameters=temperature'

# feed = feedparser.parse(url)

day = datetime.today().weekday()

päivät = ['Maanantai','Tiistai','Keskiviikko','Torstai','Perjantai','Lauantai','Sunnuntai']

# sää = feed.entries[0].summary_detail.value

# print(sää)

paikkakunnatPath = "valitutPaikkakunnat.txt"
paikkakunnat = []

def WriteToLog(timestamp, location, temperature):
    logPath = "log.txt"
    if not os.path.exists(logPath):
         with open(logPath, 'a') as pk:
            pk.write("Loki:" + '\n')
    log_entry = f"{timestamp} - {location}: {temperature}\n"
    with open(logPath, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)


def Begin():
    if not os.path.exists(paikkakunnatPath):
        with open(paikkakunnatPath, 'a') as pk:
            pk.write("" + '\n')
    
    if not paikkakunnat:
        with open(paikkakunnatPath, 'r', encoding='utf-8') as pk:
            for line in pk:
                paikkakunnat.append(line.strip())
    print("Nyt on", päivät[day], datetime.now())
    print("Valitut paikkakunnat: ")
    for pk in paikkakunnat:
        print(pk)
    textInput = ""
    while textInput != "x":
        textInput = input("Haluatko muuttaa seurattavia paikkakuntia? 'k','x'")
        if textInput == "k":
            paikkakunnat.clear()
            while textInput != "x":
                textInput = input("Syötä uusi paikkakunta. Lopeta syöttämällä 'x'")
                if textInput == "x":
                    break
                else:
                    paikkakunnat.append(textInput)
        else:
            break
    
    print("Valitut paikkakunnat: ")
    for pk in paikkakunnat:
        print(pk)
    with open(paikkakunnatPath, 'w', encoding='utf-8') as pk_file:
        for paikkakunta in paikkakunnat:
            pk_file.write(paikkakunta + '\n')  # Writes each item on a new line

    textInput = ""
    while textInput != "x":
        textInput = input("Haluatko hakea lämpötilatiedon Ilmatieteenlaitokselta? 'k' 'x'")
        if textInput == "k":
            HaeLämpöTilat(paikkakunnat)
            break
        else:
            print("Et halunnut hakea tietoja..")



#tähän piti kyllä käyttää chatgpt:een apua, en saanut haettua dataa ilmatieteen sivulta ja niiden ohjeet on aika sekavat.
def HaeLämpöTilat(paikkakunnat):
    success = 0
    for pk in paikkakunnat:
        url = f"https://opendata.fmi.fi/wfs?service=WFS&version=2.0.0&request=getFeature&storedquery_id=fmi::observations::weather::simple&place={pk}&parameters=temperature"
        response = requests.get(url)

        if response.status_code == 200:
            root = ElementTree.fromstring(response.content)

            lämpötilat = []
            for member in root.findall(".//wfs:member", namespaces):
                param_name = member.find(".//BsWfs:ParameterName", namespaces)
                param_value = member.find(".//BsWfs:ParameterValue", namespaces)
                time_elem = member.find(".//BsWfs:Time", namespaces)

                if param_name is not None and param_value is not None and time_elem is not None:
                    if param_name.text == "temperature":
                        aika = time_elem.text
                        lämpötila = float(param_value.text)
                        lämpötilat.append((aika, lämpötila))

            if lämpötilat:
                viimeisin = max(lämpötilat, key=lambda x: x[0])  # Uusin mittaus
                timestamp = datetime.strptime(viimeisin[0], "%Y-%m-%dT%H:%M:%SZ")
                formatted_timestamp = timestamp.strftime("%d.%m.%Y %H:%M")
                temperature = viimeisin[1]
                print(f"{pk:<10} {temperature:>10}°C   ({formatted_timestamp})")
                WriteToLog(formatted_timestamp,pk,f"{temperature}°C")
                success += 1
            else:
                WriteToLog(formatted_timestamp,pk,"Haku virhe")
                print(f"{pk}: Ei löydy lämpötilatietoa")
        else:
            WriteToLog(formatted_timestamp,pk,"Haku virhe")

    WriteToLog(datetime.now(),success," paikkakunnan lämpötilat haettiin onnistuneesti")

Begin()

