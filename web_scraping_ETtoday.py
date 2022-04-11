from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages =set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")





# pages = set()
# def NextPage_links
#     global pages
#     html = requests.get()
#     bs_obj = BeautifulSoup(html.text, features="html.parser")
#     box = bs_obj.findAll
#         html = requests.get("https://sports.ettoday.net" + url)
#         bs_obj = BeautifulSoup(html)
#         for link in bs_obj.findAll('a', href=re.compile('^(/wiki/)')):
#             if link.attrs['href'] not in pages: #新頁面
#                 newPage = link.attrs['href']
#                 print(newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)
#
# NextPage_links('')