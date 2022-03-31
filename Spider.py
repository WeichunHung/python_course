from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError
def getTitle(url):
    try:
        html = requests.get(url)
        bs_obj = BeautifulSoup(html.text, features="html.parser")
        list = bs_obj.select('div.r-ent div.title a')
        for ele in list:
            if '公告' not in ele.text:
                print(ele.text)
                print('link: ', 'https://www.ptt.cc/'+ele.get('href'))
                html = requests.get('https://www.ptt.cc'+ele.get('href'))
                bs_obj = BeautifulSoup(html.text, features="html.parser")
                metaline = bs_obj.find_all('span',{'class':'article-meta-value'})
                print('author: ', metaline[0].text)
                print('time: ', metaline[3].text )
                commenter = bs_obj.find('span',{'class':'f3 hl push-userid'})
                comment = bs_obj.find('span',{'class':'f3 push-content'})
                print('comment: ',commenter.text,comment.text)
    except HTTPError as e:
        return None

getTitle("https://www.ptt.cc/bbs/NBA/index6508.html")
