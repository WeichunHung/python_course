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
        article_links = 'https://www.ptt.cc' + ele.get('href')
        print('Article Link: ', article_links)

    for link in suggest.findAll('a'):
        print(set('https://www.ptt.cc' + link.get('href')))







getLink("https://www.ettoday.net/news/20220405/2223050.htm")