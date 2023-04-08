import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
data = soup.select('div.some-class span.some-data')

with open('data.csv','w',newline = '') as file:
  writer = csv.writer(file)
  writer.writerow(['Data'])
  for item in data:
    writer.writerow([item.text])
