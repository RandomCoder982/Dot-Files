import requests
from lxml import etree

url = "https://weather.com/en-IN/weather/today/l/60f76bec229c75a05ac18013521f7bfb52c75869637f3449105e9cb79738d492"

response = requests.get(url)

if response.status_code == 200:
    dom = etree.HTML(response.text)
    elements = dom.xpath("//span[@data-testid='TemperatureValue' and contains(@class,'CurrentConditions')]")

    if elements:
        temperature = elements[0].text
        print(f"The current temp is: {temperature}")
    else:
        print("Temp not found")
else:
    print("Failed to fetch webpage")


