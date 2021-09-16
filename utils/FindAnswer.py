class FindAnswer:
    def __init__(self, db):
        self.db = db

    def _find_tag_value(self, pk):
        H_info = {}
        h_info_sql = """
                     select * from Hospital, Hos_subject, Location
                     where Hospital.병원_번호 = Hos_subject.병원_번호 = Location.병원_번호 and Hospital.병원_번호 = %d
                     """ % (pk)
        db_answer_one = self.db.select_one(h_info_sql)
        db_answer_all = self.db.select_all(h_info_sql)
        H_info['A_name'] = db_answer_one['이름']
        H_info['A_Type'] = db_answer_one['Type']
        H_info['A_med_cnt'] = db_answer_one['의료인_수']
        H_info['A_Tel'] = db_answer_one['전화번호']
        H_info['A_lisense'] = db_answer_one['인허가일자']
        H_info['A_Location'] = db_answer_one['city_name'] + ' ' + db_answer_one['s_c'] + ' ' + db_answer_one['rest']
        subject = ''
        for sub in db_answer_all:
            subject += sub['과목명'] + ' '
            H_info['A_Subject'] = subject
        return H_info

    # 검색 쿼리 생성
    def _make_query(self, intent_name, ner_tags):
        sql = "select * from Predict"
        if intent_name == '인사' or intent_name == '코로나':
            where = " where intent='{}' ".format(intent_name)
        else:
            where = ' where intent="%s" and ' % intent_name
            if len(ner_tags) == 1:
                where += 'ner="%s"' % ner_tags[0]
            elif len(ner_tags) == 2:
                where += "ner = '{0},{1}'".format(ner_tags[0], ner_tags[1])
            elif len(ner_tags) == 3:
                where += "ner = '{0},{1},{2}'".format(ner_tags[0], ner_tags[1], ner_tags[2])
        sql = sql + where
        return sql

    # 답변 검색
    def search(self, intent_name, ner_tags):
        # 의도명, 개체명으로 답변 검색
        sql = self._make_query(intent_name, ner_tags)
        answer = self.db.select_one(sql)
        # 검색되는 답변이 없으면 의도명만 검색
        if answer is None:
            sql = self._make_query(intent_name, None)
            answer = self.db.select_one(sql)

        return (answer['answer'], answer['answer_image'])

    # NER 태그를 실제 입력된 단어로 변환
    def tag_to_word(self, intent_name, ner_predicts, answer):
        H_num = []; where = ""
        sql = """
                select Hospital.병원_번호 from Hospital, Location 
                where Hospital.병원_번호 = Location.병원_번호 and 
              """

        if intent_name == '정보':
            for word, tags in ner_predicts:
                if tags == 'B_Hospital':
                    where += ' 이름 = "%s"' % word
                elif tags == 'B_City' :
                    where += ' city_name = "%s" and ' % word
            sql = sql + where

            db_answer = self.db.select_all(sql)
            for field in db_answer :
                H_num.append(field['병원_번호'])

        if len(H_num) > 1 : answer = '검색되는 병원 많음'
        else :
            for pk in H_num:
                Hospital_INFO = self._find_tag_value(pk)
            for answer_tag in Hospital_INFO:
                answer = answer.replace(answer_tag, Hospital_INFO[answer_tag])



        #             h_num_sql = """
        #                         select 병원_번호 from Hospital where 이름 = "%s"
        #                         """ % (word)
        #             db_answer = self.db.select_all(h_num_sql)
        #             for field in db_answer:
        #                 H_num.append(field['병원_번호'])
        #
        #     if len(H_num) > 1 : answer = '검색되는 병원 많음'
        #     else :
        #         for pk in H_num:
        #             Hospital_INFO = self._find_tag_value(pk)
        #         for answer_tag in Hospital_INFO:
        #             answer = answer.replace(answer_tag, Hospital_INFO[answer_tag])
        #
        answer = answer.replace('{', '')
        answer = answer.replace('}', '')
        return answer