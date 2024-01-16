from bs4 import BeautifulSoup
import requests as req

url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%9A%B0%EC%9A%B8%EC%A6%9D&sort=0&photo=0&field=0&pd=3&ds=2022.01.01&de=2022.12.31&cluster_rank=38&mynews=0&office_type=0&office_section_code=0&news_office_checked=&office_category=0&service_area=0&nso=so:r,p:from20220101to20221231,a:all&start=1'

res = req.get(url) 
soup = BeautifulSoup(res.text)

a= soup.find("div", "api_txt_lines.dsc_txt")
a
'''
#news_title = soup.select('div','api_txt_lines.tit')

news_sub = soup.select('div.dsc_wrap')
news_sub_s = soup.find('div', attrs={'class':'api_txt_lines.dsc_txt'})

#news_sub = soup.find_all('div', attrs={'class':'api_txt_lines dsc'})
print(news_title)
print(news_sub[0].text)
print(news_sub_s)
#print(news_sub)
'''
import pandas
from bs4 import BeautifulSoup
import requests as req
import By


def naver_news_crawler(page):
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%9A%B0%EC%9A%B8%EC%A6%9D&sort=0&photo=0&field=0&pd=3&ds=2022.01.01&de=2022.12.31&cluster_rank=38&mynews=0&office_type=0&office_section_code=0&news_office_checked=&office_category=0&service_area=0&nso=so:r,p:from20220101to20221231,a:all&start={page-1}1'
    
    res = req.get(url) 
    soup = BeautifulSoup(res.text, 'html.parser')

    news_sub = soup.select('div.dsc_wrap')


    print(news_sub[0].text)

    
    return 


naver_news_crawler(1)

# 크롤링할 검색어와 페이지 수 지정
search_query = '코로나'
page_number = 1

# 크롤링 실행
naver_news_crawler(search_query, page_number)

