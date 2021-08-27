from utils.Preprocess import Preprocess

sent = "의료법인 은혜와감사의료재단 향남스마트병원"

p = Preprocess(userdic='../utils/user_dic.txt') # 사용자 사전

pos = p.pos(sent) # 제외시킬 품사 // 형태소단위로 끊은 형태 (품사가 아직 제외가 안됨)!

# ret = p.get_keywords(pos, without_tag= False)
# print(pos)
# print(ret)
#
# # 태그 없이 단어만 추출
print(pos)
# ret = p.get_keywords(pos, without_tag= True)
# print(ret)