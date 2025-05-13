#### Dette er et testscript for å spørre etter og behandle data fra SSBs API.
#### Marker kode og trykk "Shift + Enter" for å kjøre den valgte koden.

######## Laste nødvendige (standard-)pakker

import requests  # For å kjøre spørringer mot alle mulige APIer ++
import pandas as pd  # For å håndtere data i tabellform. Standard i "Data science"
from pyjstat import pyjstat  # Anbefalt av SSB for å håndtere JSON-stat2 formatet

######## Hente data fra SSB API

# Endepunkt for SSB API
url = "https://data.ssb.no/api/v0/no/table/11607/"

# Spørring fra SSB API (hentet fra "API-spørring for denne tabellen" etter søk i Statistikkbanken)
query = {
    "query": [
        {
            "code": "Region",
            "selection": {
                "filter": "item",
                "values": ["3020", "3021", "3022"]
            }
        },
        {
            "code": "Alder",
            "selection": {
                "filter": "item",
                "values": ["15-74"]
            }
        },
        {
            "code": "Kjonn",
            "selection": {
                "filter": "item",
                "values": ["0", "2", "1"]
            }
        },
        {
            "code": "Landbakgrunn",
            "selection": {
                "filter": "item",
                "values": ["tot"]
            }
        },
        {
            "code": "ContentsCode",
            "selection": {
                "filter": "item",
                "values": ["Sysselsatte2"]
            }
        },
        {
            "code": "Tid",
            "selection": {
                "filter": "item",
                "values": ["2022", "2023"]
            }
        }
    ],
    "response": {
        "format": "json-stat2"
    }
}
######## Spørring vha. "requests"-modulen (Promt til ChatGPT: "Gi meg Python-kode for å hente data fra SSBs API ved hjelp av følgende kode: [limte inn alt over denne linjen]")

# Send POST-forespørselen
response = requests.post(url, json=query)

# Sjekk om forespørselen var vellykket
if response.status_code == 200:
    print("Forespørsel vellykket!")

    # Last JSON-stat2-data direkte til Dataset-objektet
    dataset = pyjstat.Dataset(response.json())

    # Konverter dataset til pandas DataFrame
    df = dataset.write("dataframe")

    # Skriv ut DataFrame for å verifisere data
    print(df.head())

    # Fortsett med å bruke df
    df.info()
    df.to_csv("ssb_data_AndrePandre.csv", index=False)
else:
    print(f"Feil ved henting av data. Statuskode: {response.status_code}")
    print(response.text)
