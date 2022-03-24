from email.header import Header
from encodings import utf_8
from types import AsyncGeneratorType
from urllib import response
import urllib.request as req
import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/PC_Shopping/index.html"
Headers = {Your User Agent}

r = requests.get(url,headers = Headers)
soup = BeautifulSoup(r.text, 'html.parser')
titles = soup.find_all("div", class_="title")

def PData(self):
    return titles
    