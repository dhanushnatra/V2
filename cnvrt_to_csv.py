from requests import get
from csv import DictWriter
from os import getenv
from dotenv import load_dotenv
load_dotenv()
api_key=getenv("API_KEY")
base_url="https://www.alphavantage.co/query?"
def get_data():
    response=get(base_url,params={"function":"NEWS_SENTIMENT","apikey":api_key,"tickers":"AAPL"})
    if response.status_code==200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
def save_to_csv(data,filename):
    if data:
        with open(filename
                ,"w",newline="") as f:
            writer=DictWriter(f,fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
def it(item):
    if "bullish" in item.lower():
        return "1"
    elif "bearish" in item.lower():
        return "2"
    else:
        return "0"
def process_data(data):
    return [[item["title"],it(item["overall_sentiment_label"])] for item in data["feed"]] 
            
if __name__=="__main__":
    _=get_data()
    print(_)
    data=process_data(_)
    print(data)
    save_to_csv(data,"news_sentiment.csv")
    print("Data saved to news_sentiment.csv")