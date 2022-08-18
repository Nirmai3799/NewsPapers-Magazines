from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

req = Request("https://en.wikipedia.org/wiki/List_of_newspapers_in_India")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

\



for i in range(len(links)):
    s="'"+str(links[i])+"'"
   
    print(s)
    print(',')

