from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError
my_set = set()
def getLink(url):

    html = requests.get(url)
    bs_obj = BeautifulSoup(html.text, features="html.parser")
    box = bs_obj.findAll('div', {'class': 'block block_w'})
    print("============================1=================================")
    for x_1 in box:
        topic = x_1.findAll('h3')
        for x_2 in topic:
            topic_title = x_2.find('a').get('title')
            print(topic_title)
            topic_link = 'https://sports.ettoday.net' + x_2.find('a').get('href')
            print(topic_link)
            # topic_set = set(topic_link)
            # print(set(topic_link))
            # first_link = topic_link()
            print("============================2=================================")

            html = requests.get(topic_link)
            article_obj = BeautifulSoup(html.text, features="html.parser")
            recomm_news = article_obj.findAll('div', {'class': 'part_pictxt_5 recomm-news clearfix'})

            for y_1 in recomm_news:
                recomm_news_topic = y_1.findAll('h3')

                for y_2 in recomm_news_topic:
                    recomm_news_title = y_2.find('a').get('title')
                    print(recomm_news_title)
                    recomm_news_link = 'https://sports.ettoday.net' + y_2.find('a').get('href')
                    print(recomm_news_link)
                    my_set.add(recomm_news_title)

            print(my_set)

getLink("https://sports.ettoday.net/sport-category/%E6%A3%92%E7%90%83")