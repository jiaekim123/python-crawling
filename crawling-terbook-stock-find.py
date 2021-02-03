import sys
import csv
import requests
from time import sleep
from bs4 import BeautifulSoup

def setItem(items, book_info):
    for list in items:
        book = []
        print(list.find('td', {'class':'td_left'}).find_all('a')[0]["href"])
        print(list.find('td', {'class':'td_left'}).find_all('a')[0].get_text()) # 제목
        print(list.find_all('td', {'class':'td_num'})[0].get_text()) # 창고 재고
        print(list.find_all('td', {'class':'td_num'})[1].get_text()) # 주문 대기
        print(list.find_all('td', {'class':'td_num'})[2].get_text()) # 가재고
        title = list.find('td', {'class':'td_left'}).find_all('a')[0].get_text()
        stuff = list.find_all('td', {'class':'td_num'})[0].get_text()
        order_stay = list.find_all('td', {'class':'td_num'})[1].get_text()
        fake_stuff = list.find_all('td', {'class':'td_num'})[2].get_text()
        link = list.find('td', {'class':'td_left'}).find_all('a')[0]["href"]
        book.append(title)
        book.append(stuff)
        book.append(order_stay)
        book.append(fake_stuff)
        sleep(0.5)
        item_response = session.get(link, timeout=5) #link에서 가격을 가져옴.
        if (item_response.status_code == 200):
            html = item_response.text
            bsObject = BeautifulSoup(html, "html.parser")
            info = bsObject.find('section', {'id':'sit_ov'}).find_all('strong')
            if (len(info) > 0):
                price = info[0].get_text().split('원')[0]
                book.append(price)
            else: 
                price = 0
                book.append(price)
            print(price)
        book.append(link)
        book_info.append(book)
        print("----------------------")
        item_response.close()
    return

def login(id, password):
# 세션 만들기
    session = requests.session()
    #로그인 정보
    login_url = "http://www.terbook.co.kr/bbs/login_check.php"
    data={
        "url":"%2Fshop%2F",
        "mb_id":id,
        "mb_password":password
            
    }
    response = session.post(login_url, data=data)
    # 로그인 실행
    response.raise_for_status()
    return session

def getStuff(book_info):
    for index in range (1, 100):
        # 재고 정보 가져오기
        url = "http://www.terbook.co.kr/adm/shop_admin/itemstocklist.php?sel_ca_id=&sel_field=it_name&search=&sort1=it_stock_qty&sort2=desc&page=" + str(index)
        sleep(0.5)
        stuff_response = session.get(url, timeout=5)
        # response = requests.get(url, headers=headers, cookies=cookies)
        if (stuff_response.status_code == 200):
            html = stuff_response.text
            bsObject = BeautifulSoup(html, "html.parser")
            stuff = bsObject.find('div', {'class' : 'tbl_head01 tbl_wrap'})
            for index in range(0,2):
                items = stuff.find_all('tr', {'class':'bg' + str(index)})
                if (len(items) == 0): break
                setItem(items, book_info)
        else :
            print(stuff_response.status_code)
            break
        stuff_response.close()
    return book_info

def saveExcel(book_info):
    with open('terbook-books-stuff-info.csv', 'w', encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['상품명', '창고재고', '주문대기', '가재고', '가격', '링크'])
        writer.writerows(book_info)
    f.close
    return

if (len(sys.argv) == 3):
    session = login(sys.argv[1], sys.argv[2])
    book_info = []
    getStuff(book_info)
    saveExcel(book_info)
else :
    print("아이디와 패스워드를 입력해주세요.")