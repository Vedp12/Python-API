import json
import requests

#? API and API Key are token from = # http://api.weatherapi.com
city_name=input("Enter city name: ")
api_key=''

url=f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"

get_data=requests.get(url)
data=get_data.json()

data2=json.dumps(data,indent=4)
# print(data2)
location=data["location"]["name"]
location_region=data["location"]["region"]


wind_data = (data["current"])
print(f"{location} is city of {location_region} which located in {data["location"]["country"]}")
print(f"Which current temp is {data["current"]["temp_c"]} celcius which condition as {data["current"]["condition"]["text"]}")