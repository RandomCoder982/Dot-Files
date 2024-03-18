from bs4 import BeautifulSoup
import requests
import os, os.path, csv

url = "https://www.octoparse.com/blog/how-to-build-a-web-crawler-from-scratch-a-guide-for-beginners"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(soup)