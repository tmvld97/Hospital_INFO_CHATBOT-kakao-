from utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel

p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin',
               userdic='../utils/user_dic.txt')

intent = IntentModel(model_name='../models/intent/intent_model.h5', proprocess=p)
query = []


query.append('안녕하세용')
query.append('방가방가')
query.append('하이루')
query.append('안녕하세요')
query.append('고려병원')
query.append('고려병원 진료과목 알려줘')
query.append('고려병원 전화번호 알려줘')
query.append('김포시 고려병원 전화번호')
query.append('김포시 요양병원')
query.append('김포시 내과')
query.append('김포시 장기동 치과병원')
query.append('김포시 장기동 산부인과 병원')
query.append('코로나 확진자 알려줘 ')
query.append('코로나 확진자 정보')
query.append('김포시 고려병원')
query.append('김포에 있는 고려병원 정보 알려줘')
query.append('포천시에 있는 경기도의료원포천병원 진료과목 알려주세요')
for item in query :
    predict = intent.predict_class(item)
    predict_label = intent.labels[predict]
    print(item)
    print("***********************")
    print("의도 예측 클래스 : ", predict)
    print("의도 예측 레이블 : ", predict_label)
    print("=======================")

