import requests

try:
    response = requests.get("https://www.google.com")
    print(f"Statuskode: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"En feil oppstod: {e}")