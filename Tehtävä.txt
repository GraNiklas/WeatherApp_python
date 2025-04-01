TEE JA PALAUTA PROJEKTI ZIPATTUNA MOODLEEN

Tee Pythonilla täsmäsääohjelma, jossa on sivun alaosassa luetellut toiminnot tai toteuta oma RSS haku mistä tahansa aiheesta / palvelusta. Jälkimmäisessä tehtävässä tee myöskin lokitiedosto, jonne tallettuu onnistuneet ja epäonnistuneet haut.

- [ ] ohjelma kysyy käynnistyksen yhteydessä: "haluatko muuttaa seurattavia paikkakuntia?"

jos käyttäjä vastaa kyllä "K", kysyy ohjelma silmukassa minkä paikkakuntien säätilaa seurataan ja tallentaa käyttäjän antamat paikkakuntien nimet tietokantaan paikkakunnat-tauluun

tällöin aikaisemmat paikkakunnat poistetaan ensin taulusta
silmukka päättyy, kun käyttäjä antaa syötteen "X" 


seuraavaksi ohjelma kysyy haluatko hakea lämpötilatiedon ilmatieteenlaitokselta?
jos käyttäjä vastaa kyllä "K", ohjelma
lukee paikkakunnat-taulun rivit silmukassa
hakee ilmatieteenlaitoksen sivuilta kunkin tauluun tallennetun paikkakunnan lämpötilan

tulostaa tiedot siististi allekkain konsoli-ikkunaan "Paikkakunta - tab - lämpötila" (tab = sarkain taikka sopiva määrä välilyöntejä, jotta paikakuntien nimet sekä lämpötilat olisivat siististi allekkain)
Kirjoita myös tiedostopohjaista lokia paikkakuntakohtaisesta lämpötilahausta:
hakuajanhetki
jos käyttäjä antoi sellaisen paikkakunnan, jonka lämpötilatietoa ei löydy (eli tulee jokin virhetilanne), kirjoitetaan lokiin ko. paikkakunnan nimi sekä teksti "Hakuvirhe"

jos taas haku onnistuu, lokiin kirjoitetaan monenko paikkakunnan lämpötila tuli haettua onnistuneesti

lokia ei ylikirjoiteta (käyttäjä voi poistaa sen käsin halutessaan)

Suunnittele ohjelmaan looginen lopetustapa
Vinkki: kanattaa käyttää Pythonin Requests kirjastoa http pyyntöön.
Yritä ratkaista tehtävä itse, mutta jos jäät junnaamaan paikallesi, voit katsoa vinkkiä täältä. Älä kuitenkaan kopioi koodia sellaisenaan, vaan tutki ideaa ja tee sitten sen pohjalta omaan toteutukseesi korjaukset:
https://github.com/Point-SimoSiren/python-weather-finland/blob/master/T%C3%A4sm%C3%A4S%C3%A4%C3%A4.py