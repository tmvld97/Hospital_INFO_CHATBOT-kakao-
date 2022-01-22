import requests
import xmltodict
import json
from datetime import datetime, timedelta
# from config.GlobalParams import total_jsonObj, corona_api, diss_predict_api

# print(diss_predict_api("김포"))
# print(diss_predict_api("여주"))

#
# # resultCode
# # 결과코드
# # resultMsg
# # 결과메세지
# # numOfRows
# # 한 페이지 결과 수
# # pageNo
# # 페이지 수
# # totalCount
# # 전체 결과 수
# # SEQ
# # 게시글번호(감염현황 고유값)
# # STATE_DT
# # 기준일
# # STATE_TIME
# # 기준시간
# # DECIDE_CNT
# # 확진자 수
# # CLEAR_CNT
# # 격리해제 수
# # EXAM_CNT
# # 검사진행 수
# # DEATH_CNT
# # 사망자 수
# # CARE_CNT
# # 치료중 환자 수
# # RESUTL_NEG_CNT
# # 결과 음성 수
# # ACC_EXAM_CNT
# # 누적 검사 수
# # ACC_EXAM_COMP_CNT
# # 누적 검사 완료 수
# # ACC_DEF_RATE
# # 누적 확진률
# # CREATE_DT
# # 등록일시분초
# # UPDATE_DT
# # 수정일시분초
#
# def xml_to_json(url):
#     content = requests.get(url).content
#     dict = xmltodict.parse(content)
#     jsonString = json.dumps(dict['response']['body']['items']['item'], ensure_ascii=False)
#     json_url = json.loads(jsonString)
#     return json_url
# #
# # dissCd = 1
# #
# #
# # corona = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?' \
# #          'serviceKey=Bog2YHvLzTtptxaFrVIGt6wnrqPUlq722t3FSu50vdFwRZQMkb8q9ANWj0ZkeKa%2BZb1vZNbaqm0yIRrCjkfJDA%3D%3D'
# #
# #
# predict_url = 'http://apis.data.go.kr/B550928/dissForecastInfoSvc/getDissForecastInfo?serviceKey=' \
#               'Bog2YHvLzTtptxaFrVIGt6wnrqPUlq722t3FSu50vdFwRZQMkb8q9ANWj0ZkeKa%2BZb1vZNbaqm0yIRrCjkfJDA%3D%3D&numOfRows=1000&pageNo=1&type=xml&'
#
# end_day = str(datetime.today().date()).replace('-','')
# predict_diss = []; predict_INFO = {};
# predict_INFO['risk'] = 0
#
# Diss_city_code = {'수원시' : 41111,'성남시' : 41131}
# word = '수원시'
# word1 = '수원'
# key = ''
# temp = [i for i in Diss_city_code.keys()]
# #[수원시,성남시]
#
# for i in range(0,len(temp)) :
#     if temp[i].startswith(word1) :
#         key = temp[i]
#
# for i in range(1, 6) :
#     option = 'dissCd={0}&znCd=41'.format(i)
#     predict_diss += xml_to_json(predict_url + option)
#
# for tag in predict_diss :
#     if tag['dt'] == end_day and tag['lowrnkZnCd'] == str(Diss_city_code[key]):
#         if int(tag['risk']) > predict_INFO['risk'] :
#             predict_INFO['risk'] = int(tag['risk'])
#
#
#
# for tag in predict_diss :
#     if tag['dt'] == end_day and tag['lowrnkZnCd'] == '41570' :
#
#
#     print(tag['dt'][:4] + '-' + tag['dt'][4:6] + '-' + tag['dt'][-2:])
#
#
# start_day = str((datetime.today() - timedelta(1)).date()).replace('-','')
# end_day = str(datetime.today().date()).replace('-','')
#
# control = '&startCreateDt={0}&endCreateDt={1}'.format(start_day,end_day)
# corona = corona + control
# corona_json = xml_to_json(corona)
#
#
# corona_INFO = {}
#
#
# if len(corona_json) == 2 : # 오늘자 업데이트 됐을 시
#     for tag in corona_json :
#         if tag['stateDt'] == end_day :
#             corona_INFO['A_stateDt'] = tag['stateDt'][:4] + '-' + tag['stateDt'][4:6] + '-' + tag['stateDt'][6:]
#             corona_INFO['A_stateTime'] = tag['stateTime']
#             corona_INFO['A_decideCnt'] = tag['decideCnt']
#             corona_INFO['A_clearCnt'] = tag['clearCnt']
#             corona_INFO['A_examCnt'] = tag['examCnt']
#             corona_INFO['A_deathCnt'] = tag['deathCnt']
#             corona_INFO['A_careCnt'] = tag['careCnt']
#             corona_INFO['A_resutlNegCnt'] = tag['resutlNegCnt']
#             corona_INFO['A_accExamCnt'] = tag['accExamCnt']
#             corona_INFO['A_accExamCompCnt'] = tag['accExamCompCnt']
#             rate = float(tag['accDefRate'])
#             rate = round(rate,2)
#             corona_INFO['A_accDefRate'] = str(rate) + '%'
# else :  # 아직 업데이트 안됐을 시
#             corona_INFO['A_stateDt'] = corona_json['stateDt'][:4] + '-' + corona_json['stateDt'][4:6] + '-' + corona_json['stateDt'][6:]
#             corona_INFO['A_stateTime'] = corona_json['stateTime']
#             corona_INFO['A_decideCnt'] = corona_json['decideCnt']
#             corona_INFO['A_clearCnt'] = corona_json['clearCnt']
#             corona_INFO['A_examCnt'] = corona_json['examCnt']
#             corona_INFO['A_deathCnt'] = corona_json['deathCnt']
#             corona_INFO['A_careCnt'] = corona_json['careCnt']
#             corona_INFO['A_resutlNegCnt'] = corona_json['resutlNegCnt']
#             corona_INFO['A_accExamCnt'] = corona_json['accExamCnt']
#             corona_INFO['A_accExamCompCnt'] = corona_json['accExamCompCnt']
#             rate = float(corona_json['accDefRate'])
#             rate = round(rate,2)
#             corona_INFO['A_accDefRate'] = str(rate) + '%'
#
#
#
# predict_url = xml_to_json(predict_url)
#
#
