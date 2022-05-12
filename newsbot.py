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

    result = list_title[0] + " - " + list_company[0] + "\n" + list_href[0] + "\n\n" + list_title[1] + " - " + list_company[1] + "\n" + list_href[1] + '''\n
''' + list_title[2] + " - " + list_company[2] + "\n" + list_href[2] + "\n\n" + list_title[3] + " - " + list_company[3] + "\n" + list_href[3] + '''\n
''' + list_title[4] + " - " + list_company[4] + "\n" + list_href[4] + "\n\n" + list_title[5] + " - " + list_company[5] + "\n" + list_href[5] + '''\n
''' + list_title[6] + " - " + list_company[6] + "\n" + list_href[6] + "\n\n" + list_title[7] + " - " + list_company[7] + "\n" + list_href[7] + '''\n
''' + list_title[8] + " - " + list_company[8] + "\n" + list_href[8] + "\n\n" + list_title[9] + " - " + list_company[9] + "\n" + list_href[9] + '''\n
''' + list_title[10] + " - " + list_company[10] + "\n" + list_href[10] + "\n\n" + list_title[11] + " - " + list_company[11] + "\n" + list_href[11] + '''\n
''' + list_title[12] + " - " + list_company[12] + "\n" + list_href[12] + "\n\n" + list_title[13] + " - " + list_company[13] + "\n" + list_href[13] + '''\n
''' + list_title[14] + " - " + list_company[14] + "\n" + list_href[14] + "\n\n" + list_title[15] + " - " + list_company[15] + "\n" + list_href[15] + '''\n
''' + list_title[16] + " - " + list_company[16] + "\n" + list_href[16] + "\n\n" + list_title[17] + " - " + list_company[17] + "\n" + list_href[17] + '''\n
''' + list_title[18] + " - " + list_company[18] + "\n" + list_href[18] + "\n\n" + list_title[19] + " - " + list_company[19] + "\n" + list_href[19] + "\n"
  
    return result




