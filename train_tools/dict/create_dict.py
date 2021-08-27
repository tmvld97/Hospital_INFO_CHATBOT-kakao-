from utils.Preprocess import Preprocess
from tensorflow.keras import preprocessing
import pickle

#말뭉치 데이터 읽어오기
def read_corpus_data(filename):
    with open(filename, 'r',encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
    return data

# 말뭉치 데이터 가져오기
corpus_data = read_corpus_data('./total_train.txt')


p = Preprocess(userdic='../../utils/user_dic.txt')
dict = []
for c in corpus_data:
    pos = p.pos(c[1])   #문장
    for k in pos:
        dict.append(k[0])   #형태소(의미있는 단어)
    # keywords = p.get_keywords(pos, without_tag=True)
    # for k in keywords:
    #     dict.append(k)

#   word2index 생성
#   사전의 첫 번째 인덱스에는 OOV사용 , ( 단어 임베딩)    # out of vocabular

tokenizer = preprocessing.text.Tokenizer(oov_token='OOV')
tokenizer.fit_on_texts(dict)
word_index = tokenizer.word_index
print(word_index)
# 사전 파일 생성
f = open("chatbot_dict.bin", "wb")
try:
    pickle.dump(word_index, f)
except Exception as e:
    print(e)
finally:
    f.close()