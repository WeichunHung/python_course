import requests
from bs4 import BeautifulSoup
import re  # p.23
import datetime
from dateutil import relativedelta
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *
import csv


# d = datetime.strptime("2022-04-27", "%Y-%m-%d")
# d2 = d - relativedelta.relativedelta(months=1)
# last_time = parse('2022-04-27 22:08:00+08:00')

now = parse(str(datetime.now()))
oneWeek = now - relativedelta.relativedelta(days=7)
print('Present Time:',now)
print('Posts from:',oneWeek)

pages = set()
newsList = list()


def prefix_str(str):
    return str.strip().replace(u'\u3000', u' ')


def getLinks(pageUrl):

    try:
        html = requests.get(pageUrl)
        bsObj = BeautifulSoup(html.text, features="html.parser")

        for link in bsObj.findAll("a", href=re.compile('^/news/\d+')):
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    newPage = link.attrs['href']
                    if newPage.startswith('//sports.ettoday'):
                        newPage = 'https:' + newPage
                    if newPage.startswith('/news/'):
                        newPage = 'https://sports.ettoday.net' + newPage
                    html = requests.get(newPage)
                    newPage_Obj = BeautifulSoup(html.text, features="html.parser")
                    dateObj = newPage_Obj.find('time').get('datetime')
                    if parse(dateObj).replace(tzinfo=None) > oneWeek:
                        title = newPage_Obj.select('h1.title')[0].text
                        date = newPage_Obj.select('time.date')[0].text
                        if len(newPage_Obj.select('div.tag a')) > 0:
                            # tag = ', '.join(t.text for t in newPage_Obj.select('div.tag a'))
                            tag = []
                            for t in newPage_Obj.select('div.tag a'):
                                tag.append(t.text)
                            newTags = ", ".join(tag)
                        else:
                            newTags = 'None'

                        Page_dict = {'Title': prefix_str(title), 'Date': prefix_str(date), 'Link': prefix_str(newPage),
                                     'Tag': prefix_str(newTags)}
                        print(Page_dict)
                        newsList.append(Page_dict)
                        pages.add(link.attrs['href'])
                        getLinks(newPage)

                    else:
                        return
    except Exception as e:
        print(e)
    else:
        getLinks("https://sports.ettoday.net")

getLinks("https://sports.ettoday.net")

















