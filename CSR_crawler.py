import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup
import pandas as pd

async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto('https://24h.pchome.com.tw/region/DXBD')
    pageHTML = await page.content()
    bsObj = BeautifulSoup(pageHTML, features="html.parser")
    MenuObj = bsObj.find('dl',{'id':'MenuContainer'})
    # print(MenuObj.findAll('a'))

    for a in MenuObj.findAll('a'):
        title = a.text
        link = 'https:' + a.get('href')
        print(title,link)
        browser = await launch(headless=True)
        page = await browser.newPage()
        await page.goto(link)
        pageHTML = await page.content()
        PageObj = BeautifulSoup(pageHTML, features="html.parser")

        itemList = []
        for p in PageObj.findAll('div',{'class':'prod_info'}):
            price = p.find('span',{'class':'value'}).text
            itemDict = {}
            itemDict['Price']= int(price)
            # itemDict['Product']= name
            itemList.append(itemDict)

        print(itemList)
        # price = bsObj.select('span#PriceTotal')[0].text
        # print(price)
        # put the extracted prices into the set
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())


