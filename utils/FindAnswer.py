# 답변 검색 모듈
class FindAnswer:
    def __init__(self, db): # Database 인스턴스 객체를 인자로 받음
        self.db = db

    # 검색 쿼리 생성
    def _make_query(self, intent_name, ner_tags):
        sql = "select * from chatbot_train_data"
        if intent_name != None and ner_tags == None:
            sql = sql + " where intent='{}' ".format(intent_name)

        elif intent_name != None and ner_tags != None:
            where = ' where intent="%s" and ' % intent_name
            if len(ner_tags) == 1 :
                where += 'ner="%s"' % ner_tags[0]
            elif len(ner_tags) == 2 :
                where += "ner = '{0},{1}'".format(ner_tags[0],ner_tags[1])
            sql = sql + where
            print(sql)
            # if (len(ner_tags) > 0):
            #     where += 'and ('
            #     for ne in ner_tags:
            #         where += " ner like '%{}%' and".format(ne)
            #     where = where[:-4] + ')'
            # sql = sql + where

        # 동일한 답변이 2개 이상인 경우, 랜덤으로 선택
        sql = sql + " order by rand() limit 1"
        return sql

    # 답변 검색
    def search(self, intent_name, ner_tags):
        # 의도명, 개체명으로 답변 검색
        sql = self._make_query(intent_name, ner_tags)
        answer = self.db.select_one(sql)

        # 검색되는 답변이 없으면 의도명만 검색
        if answer is None:
            sql = self._make_query(intent_name, None)
            answer = self.db.select_one(sql)    # select_one - db에서 1개의 row만 가져옴

        return (answer['answer'], answer['answer_image'])

    # NER 태그를 실제 입력된 단어로 변환
    def tag_to_word(self, ner_predicts, answer):
        for word, tag in ner_predicts:

            # 변환해야하는 태그가 있는 경우 추가
            if tag == 'B_Hospital' or tag == 'B_City' or tag == 'B_S_c':
                answer = answer.replace(tag, word)

        answer = answer.replace('{', '')
        answer = answer.replace('}', '')
        return answer