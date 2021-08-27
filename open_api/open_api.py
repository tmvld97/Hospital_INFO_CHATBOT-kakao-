import requests
import xmltodict
import json
from konlpy.tag import Komoran

"""
SIGUN_CD	시군코드
SIGUN_NM	시군명
BIZPLC_NM	사업장명
REFINE_ROADNM_ADDR	소재지도로명주소
REFINE_LOTNO_ADDR	소재지지번주소
REFINE_ZIP_CD	소재지우편번호
BSN_STATE_NM	영업상태명
LOCPLC_FACLT_TELNO	소재지시설전화번호
MEDINST_ASORTMT_NM	의료기관종별명
MEDSTAF_CNT	의료인수
HOSPTLRM_CNT	입원실수
SICKBD_CNT	병상수
TREAT_SBJECT_CONT_INFO	진료과목내용정보
REFINE_WGS84_LAT	위도
REFINE_WGS84_LOGT	경도

의도
인사 - 0 
정보제공 - 1
병원전체 정보제공 - 1-1
        진료과목 - 1-2
        주소 - 1-3
        전화번호 - 1-4

병원 리스트 제공 - 2 
    지역(시) 병원 리스트 - 2-1
    지역(시) + 지역(동) 병원리스트 - 2-2
    지역(시) + 의료기관종 병원리스트 - 2-3
    지역(시) + 진료과목 병원리스트 - 2-4

# 길찾기, 기타등등
"""


def remove_redundancy(list_A):  # list 중복제거 함수
    set_list = set(list_A)
    remove_list = list(set_list)
    return remove_list



# """
url = "https://openapi.gg.go.kr/GgHosptlM?KEY=337b4bebd30e4d419b85a1ba8c9c26a2&pSize=1000"
url2 = "https://openapi.gg.go.kr/GgHosptlM?KEY=337b4bebd30e4d419b85a1ba8c9c26a2&pIndex=2&pSize=1000"
content = requests.get(url).content
content2 = requests.get(url2).content

dict = xmltodict.parse(content)
dict2 = xmltodict.parse(content2)

jsonString = json.dumps(dict['GgHosptlM']['row'], ensure_ascii=False)  # <GgHosptlM> 태그의 <row> 정보
jsonString2 = json.dumps(dict2['GgHosptlM']['row'], ensure_ascii=False)

jsonObj = json.loads(jsonString)
jsonObj2 = json.loads(jsonString2)

hospital = []; hospital_1 = []
u_d = open('../utils/user_dic.txt', 'a', encoding= 'utf-8')
for tag in jsonObj2:
    if tag['BIZPLC_NM'][:5] == '의료법인 ' :
        hospital.append(tag['BIZPLC_NM'][5:])
    elif tag['BIZPLC_NM'][:4] == '의료법인' :
        hospital.append(tag['BIZPLC_NM'][4:])

for item in hospital :
    if item[2:7] == '의료재단 ' :
            hospital_1.append(item[7:])
    elif item[2:6] == '의료재단' :
            hospital_1.append(item[6:])
    else :
            hospital_1.append(item)

for item in hospital_1 :
    if '의료재단' not in item :
        u_d.write(item + '\t' + 'NNG' + '\n')
    else :
        print(item)
# for item2 in hospital_1 :
#     u_d.write(item2 + '\t' + 'NNG' + '\n')

