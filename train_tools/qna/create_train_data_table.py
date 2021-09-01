import pymysql
import pandas as pd
from config.DatabaseConfig import *

db = None
try :
    db = pymysql.connect(
        host = DB_HOST, # 인스턴스 클릭 후 엔드포인트
        user = DB_USER,
        passwd = DB_PASSWORD,  # 자신이 설정한 패스워드
        db = DB_NAME,   # 디비이름
        port = DB_PORT,
        charset = 'utf8'
    )
    print("DB Succes")

    sql = """
            select * 
            from chatbot_train_data 
          """
    # sql = """
    #         CREATE TABLE IF NOT EXISTS `chatbot_train_data` (
    #         `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    #         `intent` VARCHAR(45) NULL,
    #         `ner` VARCHAR(1024) NULL,
    #         `query` TEXT NULL,
    #         `answer` TEXT NOT NULL,
    #         `answer_image` VARCHAR(2048) NULL,
    #         PRIMARY KEY (`id`))
    #         ENGINE = InnoDB DEFAULT CHARSET=utf8
    #       """

    with db.cursor() as cursor:
        cursor.execute(sql)
        results = cursor.fetchall()

    df = pd.DataFrame(results)
    print(df)

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
        print("DB Fail")
