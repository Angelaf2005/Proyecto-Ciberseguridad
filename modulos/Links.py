import requests
from bs4 import BeautifulSoup
import openpyxl

url = 'https://es.wikipedia.org/wiki/Sergio_P%C3%A9rez'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href:
        links.append(href)

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = 'Enlaces'


for i, link in enumerate(links, 1):
    sheet.cell(row=i, column=1, value=link)


workbook.save('links.xlsx')
