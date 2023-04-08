import requests
import csv
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/C++"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'class': 'infobox vevent'})
rows = table.find_all('tr')
data = []

for row in rows:
  cols = row.find_all(['th', 'td'])
  cols = [col.text.strip() for col in cols]
  data.append([col for col in cols if col])

with open('data.csv', 'w', newline='', encoding='utf-8') as file:
  writer = csv.writer(file)
  writer.writerow(['Attribute', 'Value'])
  for item in data:
    writer.writerow(item)
