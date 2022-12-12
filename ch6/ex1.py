#

from bs4 import BeautifulSoup as bs

html =  '<h1 id="title">한빛출판네트워크</h1><div class="top"><ul class="menu"><li>' \
        '<a href="http://www.hanbit.co.kr/member/login.html" class="login">로그인</a></li></ul>' \
        '<ul class="brand"><li><a href="http://www.hanbit.co.kr/media/">한빛미디어</a></li><li>' \
        '<a href="http://www.hanbit.co.kr/academy/">한빛아카데미</a></li></ul></div>'

soup = bs(html, "html.parser")

tag_h1 = soup.h1
print(tag_h1)

tag_div = soup.div
print(tag_div)

tag_ul = soup.ul
print(tag_ul)

tag_a = soup.a
print(tag_a)
print()

tag_ul_all = soup.find_all("ul")
# print(tag_ul_all)
for tagul in tag_ul_all :
    print("## %s" %(tagul))

# tag_a_all = soup.find_all("a")
# for tag_a in tag_a_all :
#     print("## %s" %(tag_a))
# print()
#
# tag_a = soup.a
# print(tag_a.attrs)
# print(tag_a['href'])
# print(tag_a['class'])

# tag_ul2 = soup.find('ul', attrs={'class' : 'brand'})
# print(tag_ul2)

title = soup.find(id="title")
print(title.string)

li_list = soup.select('div > ul.brand > li')
print(li_list)

for li in li_list :
    print(li.string)
