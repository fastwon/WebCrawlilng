# -*- coding:utf-8 -*-
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup


# 검색어 입력했을 때,
# 관련 뉴스 내용 5페이지까지의 뉴스 제목들을 콘솔에 출력

q = quote(input("검색어 : "))

num = 1

while num < 42:
    url = f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={q}&start={num}"
    
    response = requests.get(url)
    # print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        ul = soup.select_one('ul.list_news')
        titles = ul.select('li > div > div > a')
        
        print(f"================{int((num + 9) / 10)}페이지>>")
        
        for title in titles:
            print(title.text)
            print("----------------------------------------------------------------")
        
        num = num + 10
    
    else:
        print(response.status_code)

