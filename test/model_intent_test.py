from utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel

p = Preprocess(word2index_dic='/workspace/TEST/train_tools/dict/chatbot_dict.bin',
               userdic='/workspace/TEST/utils/user_dic.txt') # 사용자 사전

intent = IntentModel(model_name='/workspace/TEST/models/intent/2_intent_model.h5', proprocess=p)
query = []
query.append('김포시 산부인과 알려줘')
query.append('도움말 보여주세요!')
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
# query.append('도움!')
# query.append('도움말')
# query.append('헬프')
# query.append('도와줘')
# query.append('오늘 코로나 확진자')
# query.append('코로나 확진자 몇명이야?')
# query.append('코로나 사망자 몇명?')

for item in query :
    predict = intent.predict_class(item)
    predict_label = intent.labels[predict]
    print(item)
    print("***********************")
    print("의도 예측 클래스 : ", predict)
    print("의도 예측 레이블 : ", predict_label)
    print("=======================")

