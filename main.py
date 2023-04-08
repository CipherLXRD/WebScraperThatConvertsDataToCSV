import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.example.com"#the website you want to use such as 'https://en.wikipedia.org/wiki/Python_(programming_language)'
response = requests.get(url)
data = soup.select('div.some-class span.some-data')#the classes from which you want to extract your data 'mw-parser-output'

with open('data.csv','w',newline = '') as file:
  writer = csv.writer(file)
  writer.writerow(['Data'])
  for item in data:
    writer.writerow([item.text])
