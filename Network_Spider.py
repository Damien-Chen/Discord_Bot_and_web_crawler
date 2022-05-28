from email.header import Header
from encodings import utf_8
from urllib import response
import urllib.request as req
import requests
import Global
import time
import discord
from bs4 import BeautifulSoup

Global.initialize()

#Get titles
url = "https://www.ptt.cc/bbs/PC_Shopping/index.html"
Headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",}
r = requests.get(url,headers = Headers)
soup = BeautifulSoup(r.text, 'html.parser')
titles = soup.find_all("div", class_="title")



#Get the number of titles
Global.list = []
Global.link = []
for title in titles:
    if title.a != None:     
        Global.list.append(title.a.string)
        Global.link.append(title.a['href'])
        time.sleep(0.1)
        Global.num += 1


#for i in range(len(Global.list)):
  #  print(Global.list[Global.i])
  # print(Global.link[Global.i])
  #  Global.i += 1 
  #  time.sleep(1)
        

#Return titles
def PData(self):
    for title in titles:
        if title.a != None:
            return (Global.list[Global.i],Global.link[Global.i])

    
