import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import preprocessing
from config.GlobalParams import HOS_SUBJECT, HOS_TYPE, HOS_TEL, HOS_LOC

# 개체명 인식 모델 모듈
class NerModel:
    def __init__(self, model_name, proprocess):

        # BIO 태그 클래스 별 레이블
        self.index_to_ner = {1: 'O', 2: 'B_Hospital', 3: 'B_City', 4: 'B_Treat', 5: 'B_S_c', 6: 'B_Type', 7: 'B_Subject', 8: 'B_Location', 9: 'B_Tel', 0: 'PAD'}

        # 의도 분류 모델 불러오기
        self.model = load_model(model_name)

        # 챗봇 Preprocess 객체
        self.p = proprocess


    # 개체명 클래스 예측
    def predict(self, query):
        # 형태소 분석
        pos = self.p.pos(query)

        # 문장내 키워드 추출(불용어 제거)
        keywords = self.p.get_keywords(pos, without_tag=True)
        sequences = [self.p.get_wordidx_sequence(keywords)]

        # 패딩처리
        max_len = 11
        padded_seqs = preprocessing.sequence.pad_sequences(sequences, padding="post", value=0, maxlen=max_len)

        predict = self.model.predict(np.array([padded_seqs[0]]))
        predict_class = tf.math.argmax(predict, axis=-1)

        tags = [self.index_to_ner[i] for i in predict_class.numpy()[0]]

        for i, key in enumerate(keywords) :
            if key in HOS_TYPE :
                tags[i] = 'B_Type'
            elif key in HOS_SUBJECT :
                tags[i] = 'B_Subject'
            elif key in HOS_LOC :
                tags[i] = 'B_Location'
            elif key in HOS_TEL :
                tags[i] = 'B_Tel'
        return list(zip(keywords, tags))

    def predict_tags(self, query):
        # 형태소 분석
        pos = self.p.pos(query)

        # 문장내 키워드 추출(불용어 제거)
        keywords = self.p.get_keywords(pos, without_tag=True)
        sequences = [self.p.get_wordidx_sequence(keywords)]

        # 패딩처리
        max_len = 11
        padded_seqs = preprocessing.sequence.pad_sequences(sequences, padding="post", value=0, maxlen=max_len)

        predict = self.model.predict(np.array([padded_seqs[0]]))
        predict_class = tf.math.argmax(predict, axis=-1)

        np_predict = predict_class.numpy()[0]
        for i, key in enumerate(keywords) :
            if key in HOS_TYPE :
                np_predict[i] = 6
            elif key in HOS_SUBJECT :
                np_predict[i] = 7
            elif key in HOS_LOC :
                np_predict[i] = 8
            elif key in HOS_TEL :
                np_predict[i] = 9

        tags = []; count = 0

        for tag_idx in np_predict:
            if tag_idx == 1: continue
            tags.append(self.index_to_ner[tag_idx])

        if len(tags) == 0: return ['None']
        return tags


