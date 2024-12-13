import requests
import json

#? API and API Key are token from = # https://newsapi.org 

api_key=""
url=f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api_key}"

response= requests.get(url)
data= response.json()
# print(data)
if response.status_code == 200:
    total_news=data["totalResults"]
    print(f"Total number of news: {total_news}")
    
    
    #? For loop to get number of news
    numofnews=int(input("Enter number of news: "))
    for i1 in range(numofnews):
        
    #!All api request 
        print(f"\nnews no{i1+1}")
        news_title = data["articles"][i1]["title"]
        news_description = data["articles"][i1]["description"]
        numofnews+=1
        print(f"{news_title} \n")
        print(f"{news_description} \n\n")
        
