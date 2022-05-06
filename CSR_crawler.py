import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://24h.pchome.com.tw/prod/DXBD0L-A900BLIWI')
    pageHTML = await page.content()
    bsObj = BeautifulSoup(pageHTML, features="html.parser")
    price = bsObj.select('span#PriceTotal')[0].text
    print(price)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())


