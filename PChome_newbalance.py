import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup
import pandas as pd

async def main():
    try:
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
            CatalogObj = BeautifulSoup(pageHTML, features="html.parser")

            for l in CatalogObj.findAll('a',{'class':'prod_img'}):
                link = 'https:' + l.get('href')
                browser = await launch(headless=True)
                page = await browser.newPage()
                await page.goto(link)
                pageHTML = await page.content()
                PageObj = BeautifulSoup(pageHTML, features="html.parser")

                itemList = []
                for a in PageObj.select('div.Cm_Cr'):
                    name = a.find('h5',{'class':'nick'}).text
                    price = a.find('span',{'id':'PriceTotal'}).text
                    itemDict = {}
                    itemDict['Product'] = name
                    itemDict['Price'] = int(price)
                    itemList.append(itemDict)
                print(itemList)
            # price = bsObj.select('span#PriceTotal')[0].text
            # print(price)
            # put the extracted prices into the set
    except Exception as e:
        print(e)
    else:
        asyncio.get_event_loop().run_until_complete(main())

        await browser.close()
asyncio.get_event_loop().run_until_complete(main())



