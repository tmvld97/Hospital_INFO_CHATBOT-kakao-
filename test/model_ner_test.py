from utils.Preprocess import Preprocess
from models.ner.NerModel import NerModel

p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin',
               userdic='../utils/user_dic.txt')

ner = NerModel(model_name='../models/ner/ner_model.h5', proprocess=p)
query = []

query.append('김포시 고려병원')
query.append('김포시 장기동 고려병원 정보')



# query.append('고려병원 정보 알려줘')
# query.append('오산시 치과 목록')
# query.append('오산시 오산한국병원 진료과목')
# query.append('오산시 오산동 산부인과 알려줘')
# query.append('오산시 오산동 신경과 알려주삼')
# query.append('김포시 장기동 요양병원 리스트')
# query.append('김포시 장기동 병원리스트')
# query.append('안녕하세요')
# query.append('하이!')
# query.append('하이!')
# query.append('안녕하세용')
# query.append('방가방가')
# query.append('고려병원 진료과목')
# query.append('고려병원 진료과목 알려줘!')
# query.append('고려병원 과목 알려주세용')
# query.append('고려병원 진료!')
# query.append('고려병원 주소 알려줘')
# query.append('고려병원 길찾기')
# query.append('고려병원 네비게이션')
# query.append('고려병원 위치 알려주세요')
# query.append('고려병원 전화번호')
# query.append('고려병원 번호좀 알려줘')
# query.append('고려병원 번호 알려주삼')
# query.append('김포시 병원 리스트')
# query.append('김포 병원 리스트')
# query.append('광주시 병원 목록')
# query.append('광주 병원 목록')
# query.append('김포시 장기동 병원 리스트')
# query.append('김포시 장기동 병원 목록')
# query.append('오산시 오산동 병원 리스트')
# query.append('김포시 요양병원 알려줘')
# query.append('김포시 장기동 치과병원 알려주삼')
# query.append('오산시 오산동 요양병원 추천')
# query.append('김포시 산부인과 병원목록')
# query.append('오산시 신경과 병원 알려줘')
# query.append('김포시 장기동 산부인과 알려줘')
# query.append('오늘 코로나 확진자')
# query.append('코로나 확진자 몇명이야?')
# query.append('코로나 사망자 몇명?')

for item in query :
    predicts = ner.predict(item)
    tags = ner.predict_tags(item)
    print(item)
    print("***********************")
    print(predicts)
    print(tags)
    print("***********************")
    print('\n')
