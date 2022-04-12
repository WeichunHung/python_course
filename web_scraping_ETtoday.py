from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

pages = set()
def getLinks(pageUrl):
    global pages
    ssl._create_default_https_context = ssl._create_unverified_context
    html = urlopen("https://sports.ettoday.net"+pageUrl)
    bsObj = BeautifulSoup(html, features="html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/news/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                html = urlopen("https://sports.ettoday.net" + newPage)
                newPage_Obj = BeautifulSoup(html, features="html.parser")
                # newTitle = newPage_Obj.select('#sport > div.wrapper > div.container > div > div.c1 > article > div > header > h1')
                newTitle = newPage_Obj.find('h1', {'class': 'title'} )
                print(newTitle.text)

                print("https://sports.ettoday.net" + newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")