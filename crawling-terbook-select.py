from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.terbook.co.kr/shop/listtype.php?type=3")

bsObject = BeautifulSoup(html, "html.parser") 


# print(bsObject) # 웹 문서 전체가 출력됩니다. 

# print(bsObject.head.title) # 타이틀을 출력합니다.

# 메타데이터의 내용을 가져와서 출력합니다.
# for meta in bsObject.head.find_all('meta'):
#     print(meta.get('content'))

# 원하는 태그 내용 가져오기
# print (bsObject.head.find("meta", {"name":"description"}))
# print (bsObject.head.find("meta", {"name":"description"}).get('content'))

# lastPage = 0
# pages = bsObject.find_all('class', {'class':'pg_page pg_end'})

# book_page_urls = []
# for list in bsObject.find_all('div', {'class':'sct_txt'}):
#     print(list)
#     print("----------------------")
#     # print(list.select('a')[0].get('href'))
#     link = list.select('a')[0].get('href')
#     book_page_urls.append(link)

# print(bsObject.select_one('#container > ul > li:nth-child(1)'))
for index in range(0, 10):
    # book = bsObject.select_one('#container > ul > li:nth-child('+str(index)+')')
    # print(book)
    price = bsObject.select_one('#container > ul > li:nth-child('+str(index)+') > div.sct_cost')
    title = bsObject.select_one('#container > ul > li:nth-child('+str(index)+') > div.sct_txt > a')
    print("타이틀 : " + str(title))
    # print("타이틀 : " + str(title["content"]))
    # print("주소 : " + str(title["href"]))
    # print("가격 : " + str(price["content"]))
    # print("가격 : " + str(price))
    # print(book.find('div', {'class' : 'sct_txt'}))
    print("----------------------")
    #container > ul > li:nth-child(1) > div.sct_cost
    #container > ul > li:nth-child(1) > div.sct_cost
    #container > ul > li:nth-child(1) > div.sct_txt > a