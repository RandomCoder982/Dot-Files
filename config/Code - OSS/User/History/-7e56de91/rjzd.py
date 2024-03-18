from bs4 import BeautifulSoup
import requests
import os, os.path, csv

url = "https://www.geeksforgeeks.org/"

response = requests.get(url)

print(f"Status Code: {response.status_code}")
print(f"Reponse: {response.text}")