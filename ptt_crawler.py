from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
cookies = {
    'over18': '1'
}
resp = requests.get(url, cookies=cookies)

def getTitle(url):
    try:
        html = requests.get(url)
        bs_obj = BeautifulSoup(html.text, features="html.parser")
        board_name = bs_obj.find_all('a', class_='board')

        for ele in board_name:
            print(ele.text)
            print('link: ', 'https://www.ptt.cc/'+ele.get('href'))
            html = requests.get('https://www.ptt.cc'+ele.get('href'))
            bs_obj = BeautifulSoup(html.text, features="html.parser")
            topic = bs_obj.find('div', class_='title')
            print(topic)
            html = requests.get('https://www.ptt.cc'+ele.get('href'))
            bs_obj = BeautifulSoup(html.text, features="html.parser")
            metaline = bs_obj.find('span', {'class': 'article-meta-value'})
            print(metaline)

    except HTTPError as e:
        return None


getTitle("https://www.ptt.cc/bbs/index.html")