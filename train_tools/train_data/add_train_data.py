import requests
import xmltodict
import json
# from config.GlobalParams import CITY
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
total_json = jsonObj + jsonObj2

def remove_redundancy(list_A) :           # list 중복제거 함수
    set_list = set(list_A)
    remove_list = list(set_list)
    return remove_list



CITY = []; hos = []
for item in total_json :
    CITY.append(item['SIGUN_NM'])
    hos.append(item['BIZPLC_NM'])

CITY = remove_redundancy(CITY)
hos = remove_redundancy(hos)

f = open('add_trans_2.txt', 'a',encoding= 'utf-8')

for item in total_json :
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 정보 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 정보 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 진찰 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 진찰 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 전문 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 전문 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 종목 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 종목 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 진료과목 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 진료과목 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 진찰과목 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 진찰과목 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 전문과목 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 전문과목 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 전문 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 전문 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 주소 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 주소 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 위치 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 위치 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 가는 길 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 가는 길 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 찾아가기 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 길찾기 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 길찾기 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 네비게이션 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 네비게이션 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 지도 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 지도 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 어디' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 어딨어' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 어떻게 가' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 가는 길' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 전화 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 번호 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 전화번호 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 전화번호 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 번호 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 전화 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 연락 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 연락 알려주세요' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 연락처 알려줘' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 연락처 알려주세요' + '\t\t' + '1' + '\n')

                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 정보' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 진찰' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 전문' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 종목' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 진료과목' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 진찰과목' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 전문과목' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 전문' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 주소' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 위치' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 가는 길' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 찾아가기' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 길찾기' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 네비게이션' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 지도' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 전화' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 전화번호' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 번호' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 연락' + '\t\t' + '1' + '\n')
                f.write('0000' + '\t' + item['SIGUN_NM'][:-1] + '에 있는 ' + item['BIZPLC_NM'] + ' 연락처' + '\t\t' + '1' + '\n')

# for tag in jsonObj :
#     for lett in letter :
#         f2.write('0000' + '\t' + tag['SIGUN_NM'] + ' ' + tag['BIZPLC_NM'] + ' ' + lett + '\t\t' + '1' + '\n')
# for tag in jsonObj2 :
#     for lett in letter :
#         f2.write('0000' + '\t' + tag['SIGUN_NM'] + ' ' + tag['BIZPLC_NM'] + ' ' + lett + '\t\t' + '1' + '\n')
# f.close()
f.close()
#









# f = open('intent_3.txt', 'a',encoding= 'utf-8')

# f.write('0000' + '\t' + '도움' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '도움말!' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '도움말' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '도움 필요해' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '도와주세요' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '도와주세요!' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '도와줘' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '도와줘!' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '도움이 필요해요' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '도움이 필요합니다' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '/도움말' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '도움이 필요하네요' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '도와주세용' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '도움이 필요하네용' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '도움이 필요!' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '도와' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '실행방법' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '실행법' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '구동방법' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '구동법' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '실행서' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '도와쥬' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '헬프' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '헬프!' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + 'help' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + 'help!' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + 'HELP' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '도우미' +'\t\t' + '3' + '\n')
# f.write('0000' + '\t' + '도움이' +'\t\t' + '3' + '\n')




# f.write('0000' + '\t' + '코로나' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나!' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '바이러스' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 바이러스' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 현황' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 현황 알려주세요' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 현황 알려줘' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '바이러스 현황' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '바이러스 현황 알려주세요' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '바이러스 현황 알려줘' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '감염자' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '국내 감염자 확인' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '국내 감염자' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '오늘 감염자 몇명이야?' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 알려줘' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '확진자' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '국내 확진자 확인' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '감염자 현황 알려주세요' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '감염자 현황 알려줘' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '확진자 현황 알려주세요' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '확진자 현황 알려줘' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 알려줘!' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 현황 알려줘!' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 진행상태' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 진행경과' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 진행상황' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 진행상태 알려줘' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 진행경과 알려줘' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 진행상황 알려줘' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 현재상황' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 현재상황 알려줘' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 현재상황 알려주세요' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 진행상태 알려주세요' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 진행경과 알려주세요' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 진행상황 알려주세요' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '확진자 몇명이야?' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '감염자 몇명이야?' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '사망자 몇명이야?' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 사망자' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 감염자' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 확진자' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '바이러스 확진자' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '바이러스 사망자' +'\t\t' + '4' + '\n')
# f.write('0000' + '\t' + '코로나 현황알려주삼' +'\t\t' + '4' + '\n')

# f.close()
