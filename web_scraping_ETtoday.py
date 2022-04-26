import requests
from bs4 import BeautifulSoup
import re  # p.23

pages = set()


def getLinks(pageUrl):
    global pages
    html = requests.get(pageUrl)
    bsObj = BeautifulSoup(html.text, features="html.parser")
    for link in bsObj.findAll("a", href=re.compile('/news/')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                if newPage.startswith('//sports.ettoday'):
                    newPage = 'https:' + newPage
                if newPage.startswith('/news/'):
                    newPage = 'https://sports.ettoday.net' + newPage

                html = requests.get(newPage)
                newPage_Obj = BeautifulSoup(html.text, features="html.parser")
                newsTitle = newPage_Obj.select('h1.title')
                for title in newsTitle:
                    title = title.text
                newsDate = newPage_Obj.select('time.date')
                for date in newsDate:
                    date = date.text
                # newsTag = newPage_Obj.select('div.tag a')
                # for tag in newsTag:
                #     tag = tag.text
                Page_dict = {'Title': title, 'Date': date, 'Link': newPage}
                print(Page_dict)
                pages.add(newPage)
                getLinks(newPage)
                # news_list = []
                # news_list.append(Page_dict)
                # print(news_list)

getLinks("https://sports.ettoday.net")

