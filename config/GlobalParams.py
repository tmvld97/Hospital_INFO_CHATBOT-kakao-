import requests
import xmltodict
import json

# 단어 시퀀스 벡터 크기
MAX_SEQ_LEN = 14
HOS_TYPE = ['요양병원', '한방병원', '종합병원', '치과병원']
HOS_SUBJECT = ['진료', '진찰', '전문', '종목', '진료과목', '진찰과목', '전문과목']
HOS_LOC = ['주소','위치','가는 길','찾아가기','길찾기','네비게이션','지도','어디','어딨','어떻게 가','어딘지','가는길','네비']
HOS_TEL = ['전화','번호','전화번호','연락','연락처']

def GlobalParams():
    global MAX_SEQ_LEN, HOS_TYPE, HOS_SUBJECT, HOS_LOC, HOS_TEL, CITY

def remove_redundancy(list_A) :           # list 중복제거 함수
    set_list = set(list_A)
    remove_list = list(set_list)
    return remove_list

url = "https://openapi.gg.go.kr/GgHosptlM?KEY=337b4bebd30e4d419b85a1ba8c9c26a2&pSize=1000"
url2 = "https://openapi.gg.go.kr/GgHosptlM?KEY=337b4bebd30e4d419b85a1ba8c9c26a2&pIndex=2&pSize=1000"
content = requests.get(url).content
content2 = requests.get(url2).content

dict = xmltodict.parse(content)
dict2 = xmltodict.parse(content2)

jsonString = json.dumps(dict['GgHosptlM']['row'], ensure_ascii=False)   # <GgHosptlM> 태그의 <row> 정보
jsonString2 = json.dumps(dict2['GgHosptlM']['row'], ensure_ascii=False)

jsonObj = json.loads(jsonString)
jsonObj2 = json.loads(jsonString2)
CITY = []

#
for tag in jsonObj :
                CITY.append(tag['SIGUN_NM'])
for tag2 in jsonObj2 :
                CITY.append(tag2['SIGUN_NM'])
city = remove_redundancy(CITY)
