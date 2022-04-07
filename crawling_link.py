from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError

def getLink(url):

    html = requests.get(url)
    bs_obj = BeautifulSoup(html.text, features="html.parser")
    box = bs_obj.findAll('div', {'class': 'block block_w'})

    for ele in box:
        h3 = ele.findAll('h3')
        print(h3)

        for ele_1 in h3:
            topic_link = 'https://sports.ettoday.net' + ele_1.find('a').get('href')
            print(topic_link)



getLink("https://sports.ettoday.net/sport-category/%E6%A3%92%E7%90%83")