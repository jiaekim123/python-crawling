from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")  

bsObject = BeautifulSoup(html, "html.parser") 


# print(bsObject) # 웹 문서 전체가 출력됩니다. 

# print(bsObject.head.title) # 타이틀을 출력합니다.

# 메타데이터의 내용을 가져와서 출력합니다.
# for meta in bsObject.head.find_all('meta'):
#     print(meta.get('content'))

# 원하는 태그 내용 가져오기
# print (bsObject.head.find("meta", {"name":"description"}))
# print (bsObject.head.find("meta", {"name":"description"}).get('content'))


# 모든 링크의 텍스트와 주소 가져오기
for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))