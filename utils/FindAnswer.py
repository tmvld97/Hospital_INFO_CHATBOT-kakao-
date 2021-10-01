from config.GlobalParams import total_jsonObj, corona_INFO, diss_predict_api

class FindAnswer:
    def __init__(self, db):
        self.db = db

    def _find_tag_value(self, pk):
        H_info = {}; where = ""
        sql = """
              select * from Hospital, Hos_subject, Location
              where Hospital.병원_번호 = Hos_subject.병원_번호 and Hospital.병원_번호 = Location.병원_번호 and (            
              """
        for idx, h_n in enumerate(pk) :
            if idx == len(pk) - 1 :
                where += " Hospital.병원_번호 = %d)" % h_n
            else :
                where += " Hospital.병원_번호 = %d or " % h_n
        sql = sql + where
        db_answer_one = self.db.select_one(sql)
        db_answer_all = self.db.select_all(sql)
        H_info['A_Type'] = db_answer_one['Type']
        H_info['A_med_cnt'] = db_answer_one['의료인_수']
        H_info['A_Tel'] = db_answer_one['전화번호']
        H_info['A_lisense'] = db_answer_one['인허가일자']
        H_info['A_City'] = db_answer_one['city_name']; H_info['A_S_c'] = db_answer_one['s_c']
        H_info['A_Location'] = db_answer_one['city_name'] + ' ' + db_answer_one['s_c'] + ' ' + db_answer_one['rest']


        h_name = []; na = ''; subject = ''
        for field in db_answer_all :
            subject += field['과목명'] + ' '
            H_info['A_Subject'] = subject
            if field['이름'] not in h_name :
                h_name.append(field['이름'])
        for name in h_name :
           for tag in total_jsonObj :
               if tag['BIZPLC_NM'] == name and tag['SIGUN_NM'] == H_info['A_City'] :
                   na += name + ' [' + tag['BSN_STATE_NM'] + ']\n'
                   H_info['A_name'] = na

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
        H_num = [];  where = ""; state = 0
        sql = """
             select Hospital.병원_번호 from Hospital, Hos_subject, Location
             where Hospital.병원_번호 = Hos_subject.병원_번호 and Hospital.병원_번호 = Location.병원_번호 and
              """
        if intent_name == '정보' or intent_name == '리스트' :
            for word, tags in ner_predicts :
                if tags == 'B_Hospital' :
                    where += ' 이름 = "%s"' % word
                elif tags == 'B_City' :
                    where += " city_name like '%{}%' and ".format(word)
                    diss_predict_INFO = diss_predict_api(word)
                    state = 1
                elif tags == 'B_S_c' :
                    where += " s_c like '%{}%' and ".format(word)
                elif tags == 'B_Type' :
                    where +=  " Type like '%{}%' ".format(word)
                elif tags == 'B_Treat' :
                    where += " 과목명 like '%{}%' ".format(word)


            sql = sql + where
            db_answer = self.db.select_all(sql)
            for field in db_answer :
                if field['병원_번호'] not in H_num :
                    H_num.append(field['병원_번호'])

            if intent_name == '정보' and len(H_num) > 1 :
                answer  = "검색되는 병원  많음"
            elif len(H_num) == 0 :
                answer = "검색되는 병원이 없습니다."
            else :
                Hospital_INFO = self._find_tag_value(H_num)
                if state == 0 :
                    for answer_tag in Hospital_INFO :
                        answer = answer.replace(answer_tag, Hospital_INFO[answer_tag])
                    for word, answer_tag in ner_predicts :
                        answer = answer.replace(answer_tag, word)
                elif state == 1 :
                    for answer_tag in Hospital_INFO :
                        answer = answer.replace(answer_tag, Hospital_INFO[answer_tag])
                    for answer_tag in diss_predict_INFO :
                        answer = answer.replace(answer_tag, str(diss_predict_INFO[answer_tag]))
                    for word, answer_tag in ner_predicts :
                        answer = answer.replace(answer_tag, word)
        elif intent_name == '코로나' :
            for answer_tag in corona_INFO :
                answer = answer.replace(answer_tag, corona_INFO[answer_tag])


        answer = answer.replace('{', '')
        answer = answer.replace('}', '')
        return answer