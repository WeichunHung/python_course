
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError



def getTitle(url):
    try:
        html = urlopen(url)

        bs_obj = BeautifulSoup(html.read(), features="html.parser")
        print(bs_obj.h1.text)
    except HTTPError as e:
        return None


getTitle("https://en.wikipedia.org/wiki/Wiki")