from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen("https://product.kyobobook.co.kr/bestseller/total?periodUri=002")

soup = bs(html.read(), "html.parser")

book_page_urls = []
for i in soup.find_all("div", {"class" : {"sub_title_wrap"}}) :
    print(i.text)
