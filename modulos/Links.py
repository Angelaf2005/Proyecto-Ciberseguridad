import requests
from bs4 import BeautifulSoup
import openpyxl
import re
def links(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
            match = re.search(regex, href)
            if match:
                links.append(match.group())
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Enlaces'


    for i, link in enumerate(links, 1):
        sheet.cell(row=i, column=1, value=link)


    workbook.save('./archivos/links.xlsx')
