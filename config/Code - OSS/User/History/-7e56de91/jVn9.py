from bs4 import BeautifulSoup
import requests
import os, os.path, csv

url = "https://weather.com/en-IN/weather/today/l/60f76bec229c75a05ac18013521f7bfb52c75869637f3449105e9cb79738d492"

response = requests.get(url)

print(f"Status Code: {response.status_code}")
print(f"Reponse: {response.text}")