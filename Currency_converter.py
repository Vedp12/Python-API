import requests

#? API and API Key are token from = # https://api.currencyapi.com
your_currency="INR"
converted_currency="USD"
api_key=""
url=(f"https://api.currencyapi.com/v3/historical?apikey={api_key}={converted_currency}&base_currency={your_currency}&date=2024-12-11")

response=requests.get(url)
data=response.json()

print(data)
code=data["data"][converted_currency]["code"]
value=data["data"][converted_currency]["value"]
converted_prize=20*value
print(value, code, converted_currency)