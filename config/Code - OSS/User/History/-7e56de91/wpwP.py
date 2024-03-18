import requests
from lxml import etree

url = "https://weather.com/weather/today/l/22a176a226cd0be1fb02a6c52af211ac83976e49c19fc184b0fedddc2941c051"

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


