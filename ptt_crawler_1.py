from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError


def getTitle(url):
    try:
        html = requests.get(url)
        bs_obj = BeautifulSoup(html.text, features="html.parser")
        boards = bs_obj.findAll('a', {'class': 'board'})

        for ele in boards:
            board_link = 'https://www.ptt.cc' + ele.get('href')
            print('board link: ', board_link)
            my_headers = {'cookie': 'over18=1;'}
            html = requests.get(board_link, headers=my_headers)
            bs_obj = BeautifulSoup(html.text, features="html.parser")
            board_label = bs_obj.find('a', {'class': 'board'})
            print('board name:', board_label.text)

            topic = bs_obj.find('div', {'class': 'title'})
            topic_link = 'https://www.ptt.cc' + topic.find('a').get('href')
            html = requests.get(topic_link, headers=my_headers)
            article_obj = BeautifulSoup(html.text, features="html.parser")
            article_title = article_obj.findAll('span', {'class': 'article-meta-value'})[2].text
            print('article title:', article_title)
            author_name = article_obj.findAll('span', {'class': 'article-meta-value'})[0].text
            print('author name:', author_name)
            comment_ele = article_obj.find('span', {'class': 'push-content'})
            if comment_ele:
                first_comment = comment_ele.text
                comment_author = article_obj.find('span', {'class': 'push-userid'}).text
                print('first comment:', first_comment, 'comment author: ', comment_author)

            print("=============================================================")

    except HTTPError as e:
        print('ERROR:', e)



getTitle("https://www.ptt.cc/bbs/index.html")
