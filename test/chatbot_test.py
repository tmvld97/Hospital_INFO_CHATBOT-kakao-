from config.DatabaseConfig import *
from utils.Database import Database
from utils.Preprocess import Preprocess


# 전처리 객체 생성
# p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin',
#                userdic='../utils/user_dic.txt')
# #
# # # 질문/답변 학습 디비 연결 객체 생성
db = Database(
    host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME, db_port=DB_PORT
)
db.connect()    # 디비 연결

# 원문
# query = ''
#
# # 의도 파악
# from models.intent.IntentModel import IntentModel
# intent = IntentModel(model_name='../models/intent/intent_model.h5', proprocess=p)
# predict = intent.predict_class(query)
# intent_name = intent.labels[predict]
#
# # 개체명 인식
# from models.ner.NerModel import NerModel
# ner = NerModel(model_name='../models/ner/ner_model.h5', proprocess=p)
# predicts = ner.predict(query)
# ner_tags = ner.predict_tags(query)
#
# print("질문 : ", query)
# print("=" * 100)
# print("의도 파악 : ", intent_name)
# print("개체명 인식 : ", predicts)
# print("답변 검색에 필요한 NER 태그 : ", ner_tags)
# print("=" * 100)
# print(len(predicts))

# db.close() # 디비 연결 끊음
#
# 답변 검색
from utils.FindAnswer import FindAnswer
#
intent_name = '도움말'
ner_tags = ['B_Type']
predicts =[('도움말', 'B_Type')]

try:

    f = FindAnswer(db)
    answer_text, answer_image = f.search(intent_name, ner_tags)

    answer, alph_text, error_code = f.tag_to_word(intent_name, predicts, answer_text, ner_tags)
    if error_code != 0 : answer_image = "https://ifh.cc/g/XU37SW.jpg"
except:
    answer = "죄송해요 무슨 말인지 모르겠어요. 조금 더 공부 할게요.\n'도움말'을 참조해주세요."
    answer_image = "https://ifh.cc/g/XU37SW.jpg"

print("답변:",answer)
print(answer_image)
print(alph_text)


db.close() # 디비 연결 끊음

