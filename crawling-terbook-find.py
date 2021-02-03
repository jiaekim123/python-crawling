import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.terbook.co.kr/shop/listtype.php?type=3")

bsObject = BeautifulSoup(html, "html.parser") 

book_info = []
for list in bsObject.find_all('li', {'class':'sct_li'}):
    book = []
    # print(list)
    print(list.find('div', {'class':'sct_txt'}).get_text()) # 제목
    print(list.find('div', {'class':'sct_basic'}).get_text()) # 타입
    print(list.find('div', {'class':'sct_cost'}).get_text()) # 가격
    print("----------------------")
    # print(list.select('a')[0].get('href'))
    title = list.find('div', {'class':'sct_txt'}).get_text()
    type = list.find('div', {'class':'sct_basic'}).get_text()
    cost = list.find('div', {'class':'sct_cost'}).get_text()
    book.append(title)
    book.append(type)
    book.append(cost)
    book_info.append(book)

with open('terbook-books-info.csv', 'w', encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['타이틀', '타입', '가격'])
    writer.writerows(book_info)
f.close