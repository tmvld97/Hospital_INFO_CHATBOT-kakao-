# 답변 검색 모듈
class FindAnswer:
    def __init__(self, db): # Database 인스턴스 객체를 인자로 받음
        self.db = db

    # 검색 쿼리 생성
    def _make_query(self, intent_name, ner_tags):
        sql = "select * from chatbot_train_data"
        if intent_name != None and ner_tags == None:














