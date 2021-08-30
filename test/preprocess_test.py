from utils.Preprocess import Preprocess
f = open('../train_tools/train_data/total_train.txt', 'r',encoding= 'utf-8')

sent = "해암요양병원 연락방법 알려주세요"

p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin',
               userdic='../utils/user_dic.txt') # 사용자 사전


pos = p.pos(sent) # 제외시킬 품사 // 형태소단위로 끊은 형태 (품사가 아직 제외가 안됨)!

# ret = p.get_keywords(pos, without_tag= False)
# print(pos)
# print(ret)
#
# # 태그 없이 단어만 추출
print(pos)
# ret = p.get_keywords(pos, without_tag= True)
# print(ret)