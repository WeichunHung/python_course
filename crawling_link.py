from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError

def getLink(url):

    html = requests.get(url)
    bs_obj = BeautifulSoup(html.text, features="html.parser")
    suggest = bs_obj.find('div', {'class': 'part_list_3'}) #推薦閱讀列表
    sug_articles = suggest.findAll('a') #推薦閱讀文章

    for ele in sug_articles:
        print(ele.get('title'))
        article_links = 'https://www.ettoday.net/' + ele.get('href')
        print('Article Link: ', article_links)

        first_article_link = 'https://www.ettoday.net/' + ele.get.find('a').get('href')
        html = requests.get(first_article_link)
        bs_obj_2 = BeautifulSoup(html.text, features="html.parser")
        suggest_2 = bs_obj_2.find('div', {'class': 'part_list_3'})
        sug_articles_2 = suggest_2.findAll('a')
        print(sug_articles_2)


    for link in suggest.findAll('a'):
        print(set('https://www.ettoday.net/' + link.get('href')))






getLink("https://www.ettoday.net/news/20220405/2223050.htm")