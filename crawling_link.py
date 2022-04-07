from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError

def getLink(url):

    html = requests.get(url)
    bs_obj = BeautifulSoup(html.text, features="html.parser")
    box = bs_obj.findAll('div', {'class': 'block block_w'})

    for ele in box:
        topics = ele.findAll('h3')
        print(topics)
        topic_link = 'https://www.ettoday.net' + topics.find('a').get('href')
        print(topic_link)




getLink("https://sports.ettoday.net/sport-category/%E6%A3%92%E7%90%83")