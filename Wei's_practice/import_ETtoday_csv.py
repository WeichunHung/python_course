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
oneDay = now - relativedelta.relativedelta(days=1)
print('Present Time:',now)
print('Posts from:',oneDay)

pages = set()
rows = []

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
                    if parse(dateObj).replace(tzinfo=None) > oneDay:
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

                        pages.add(link.attrs['href'])
                        getLinks(newPage)
                        x = prefix_str(title),prefix_str(date),prefix_str(newPage),prefix_str(newTags)
                        rows.append(x)

                    else:
                        return
    except Exception as e:
        print(e)
    else:
        getLinks("https://sports.ettoday.net")

getLinks("https://sports.ettoday.net")
print(rows)

import csv

csvFile = open('/Users/wei-chunhung/Desktop/Ettoday_webScraping.csv','w+', newline='')

try:
    writer = csv.writer(csvFile)
    writer.writerow(('Title','Date','Link','Tag'))
    for i in rows:
        writer.writerow((i))

finally:
    csvFile.close()
