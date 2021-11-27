from utils.Preprocess import Preprocess
import pickle
from utils.Preprocess import Preprocess

# 단어 사전 불러오기
f = open("../train_tools/dict/chatbot_dict.bin", "rb")
word_index = pickle.load(f)
f.close()

sent = "김포 고려병원 전화번호좀 알려주세요!"

p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin',
               userdic='../utils/user_dic.txt') # 사용자 사전


pos = p.pos(sent) # 제외시킬 품사 // 형태소단위로 끊은 형태 (품사가 아직 제외가 안됨)!

# ret = p.get_keywords(pos, without_tag= False)
# print(pos)
# print(ret)
#
# # 태그 없이 단어만 추출
print(pos)
# print(ret)
ret = p.get_keywords(pos, without_tag= True)
for word in ret:
    try:
        print(word, word_index[word])
    except KeyError:
        # 해당 단어가 사전에 없는 경우, OOV 처리
        print(word, word_index['OOV'])