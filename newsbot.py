import requests
from bs4 import BeautifulSoup

def newsflash_href(soup):       # 속보 20개의 링크를 순서대로 리스트로 반환해주는 역할

    hrefs = []
    div = soup.find("div", class_= "list_body newsflash_body")

    for dt in div.find_all("dt", class_= None):
        hrefs.append(dt.find("a")["href"])

    return hrefs

def newsflash_title(soup):       # 속보 20개의 제목을 순서대로 리스트로 반환해주는 역할
    titles = []
    div = soup.find("div", class_= "list_body newsflash_body")
    for dt in div.find_all("dt", class_= None):        
        titles.append(dt.text.strip())

    return titles

def newsflash_company(soup):        # 속보 20개의 언론사를 순서대로 리스트로 반환해주는 역할
    companies = []
    for temp in soup.select(".writing"):
        companies.append(temp.text.strip())
    
    return companies

def newsflash_main():
    list_href = []
    list_title = []
    list_company = []

    header = {'User-agent' : 'Mozila/2.0'}
    res = requests.get("https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=001", headers = header)
    html = res.text
    soup = BeautifulSoup(html, "html.parser")

    list_href = newsflash_href(soup)
    list_title = newsflash_title(soup)
    list_company = newsflash_company(soup)
 
    return list_href, list_title, list_company




