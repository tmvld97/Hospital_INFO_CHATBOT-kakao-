import requests
import xmltodict
import json

def xml_to_json(url):
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    jsonString = json.dumps(dict['response']['body']['items']['item'], ensure_ascii=False)
    json_url = json.loads(jsonString)
    return json_url

dissCd = 1
znCd = 41
corona = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?' \
         'serviceKey=Bog2YHvLzTtptxaFrVIGt6wnrqPUlq722t3FSu50vdFwRZQMkb8q9ANWj0ZkeKa%2BZb1vZNbaqm0yIRrCjkfJDA%3D%3D' \
         '&startCreateDt=20210830&endCreateDt=20210830'

predict_url = 'http://apis.data.go.kr/B550928/dissForecastInfoSvc/getDissForecastInfo?serviceKey=' \
       'Bog2YHvLzTtptxaFrVIGt6wnrqPUlq722t3FSu50vdFwRZQMkb8q9ANWj0ZkeKa%2BZb1vZNbaqm0yIRrCjkfJDA%3D%3D&numOfRows=1000&pageNo=1&type=xml&' \
       'dissCd={0}&znCd={1}'.format(dissCd, znCd)

corona = xml_to_json(corona)
predict_url = xml_to_json(predict_url)

