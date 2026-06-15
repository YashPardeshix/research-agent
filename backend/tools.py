from tavily import TavilyClient
import requests
from dotenv import load_dotenv
import os

load_dotenv()

def search(query: str) -> list[str]: 
    api_key = os.getenv("TAVILY_API_KEY")  
    client = TavilyClient(api_key)
    results = client.search(query)
    urls =[item["url"] for item in results["results"]]
    return urls

def fetch(url: str) -> str: 
    response = requests.get(url)
    return