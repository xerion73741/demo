import requests as req
from bs4 import BeautifulSoup as bs
from pprint import pprint
def crawl_news():
    news_list = []
    count = 0
    url = 'https://www.twreporter.org/tag/58e5b2660f56b40d001ae6ea'
    res = req.get(url)
    soup = bs(res.text, 'lxml')
    profix = 'https://www.twreporter.org'
    for div in soup.select('div.list-item__Container-sc-1dx5lew-0'):
        title_tag = div.select_one('div.list-item__Title-sc-1dx5lew-5')
        context = div.select_one('div.list-item__Desc-sc-1dx5lew-6')
        img = div.select_one('img')
        link = div.select_one('a')
        
        # 先抓下來再判斷是否有值, 直接抓值會抱錯
        if title_tag:
            title = title_tag.get_text(strip=True)
        else:
            title = '無標題'

        if context:
            context = context.get_text(strip=True)        
        else:
            context = '無內容'

        if img:
            img = img['src']
        else: img = '無圖片'
        
        if link:
            href = link['href']
            full_link = profix + href
        else: 
            full_link = '無連結'

        news_list.append({
            'title': title,
            'context': context,
            'img': img,
            'link': full_link,
        })
        count+=1
        if count>=10: break

    return news_list

if __name__ == "__main__":
    news_list = crawl_news()
    pprint(news_list)
