import requests
from bs4 import BeautifulSoup
import re  #p.23

pages = set()
def getLinks(pageUrl):
    global pages
    html = requests.get("https://sports.ettoday.net"+pageUrl)
    bsObj = BeautifulSoup(html.text, features="html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(\/news\/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                html = requests.get("https://sports.ettoday.net" + newPage)
                newPage_Obj = BeautifulSoup(html.text, features="html.parser")
                newTitle = newPage_Obj.select('h1.title')
                for item in newTitle:
                    print(item.text)
                # newTitle = newPage_Obj.find('h1', {'class': 'title'} )
                # print(newTitle)
                print("https://sports.ettoday.net" + newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")