import pymysql
from config.DatabaseConfig import *
from config.GlobalParams import jsonObj, jsonObj2

def remove_redundancy(list_A):  # list 중복제거 함수
    set_list = set(list_A)
    remove_list = list(set_list)
    return remove_list

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
    hos_dict = {}
    for item in jsonObj2 :
        with db.cursor() as cursor:
            hos_dict['name'] = item['BIZPLC_NM']
            hos_dict['type'] = item['BIZCOND_DIV_NM_INFO']
            hos_dict['cnt_nur'] = item['MEDSTAF_CNT']
            hos_dict['tel'] = item['LOCPLC_FACLT_TELNO']
            li = item['LICENSG_DE']
            date = li[:4] + '-' + li[4:6] + '-' + li[-2:]
            hos_dict['license'] = date
            sql = """
                    insert Hospital(이름,Type,의료인_수,전화번호,인허가일자) values("%s","%s","%s","%s","%s")
                  """%(hos_dict['name'],hos_dict['type'],hos_dict['cnt_nur'],hos_dict['tel'],hos_dict['license'])
            cursor.execute(sql)
    db.commit()

    # with db.cursor() as cursor:
    #     cursor.execute(sql)

    #     results = cursor.fetchall()
    #
    # df = pd.DataFrame(results)
    # print(df)

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
        print("DB Fail")


    # City table
    # city = [
    #     {'city_code' : 41111, 'city_name' :	'수원시'},
    #     {'city_code' : 41131, 'city_name' : '성남시'},
    #     {'city_code' : 41150, 'city_name' : '의정부시'},
    #     {'city_code' : 41171, 'city_name' : '안양시'},
    #     {'city_code' : 41190, 'city_name' : '부천시'},
    #     {'city_code' : 41210, 'city_name' : '광명시'},
    #     {'city_code' : 41220, 'city_name' : '평택시'},
    #     {'city_code' : 41250, 'city_name' : '동두천시'},
    #     {'city_code' : 41271, 'city_name' : '안산시'},
    #     {'city_code' : 41281, 'city_name' : '고양시'},
    #     {'city_code' : 41290, 'city_name' : '과천시'},
    #     {'city_code' : 41310, 'city_name' : '구리시'},
    #     {'city_code' : 41360, 'city_name' : '남양주시'},
    #     {'city_code' : 41370, 'city_name' : '오산시'},
    #     {'city_code' : 41390, 'city_name' : '시흥시'},
    #     {'city_code' : 41410, 'city_name' : '군포시'},
    #     {'city_code' : 41430, 'city_name' : '의왕시'},
    #     {'city_code' : 41450, 'city_name' : '하남시'},
    #     {'city_code' : 41461, 'city_name' : '용인시'},
    #     {'city_code' : 41480, 'city_name' : '파주시'},
    #     {'city_code' : 41500, 'city_name' : '이천시'},
    #     {'city_code' : 41550, 'city_name' : '안성시'},
    #     {'city_code' : 41570, 'city_name' : '김포시'},
    #     {'city_code' : 41590, 'city_name' : '화성시'},
    #     {'city_code' : 41610, 'city_name' : '광주시'},
    #     {'city_code' : 41630, 'city_name' : '양주시'},
    #     {'city_code' : 41650, 'city_name' : '포천시'},
    #     {'city_code' : 41670, 'city_name' : '여주시'},
    #     {'city_code' : 41800, 'city_name' : '연천군'},
    #     {'city_code' : 41820, 'city_name' : '가평군'},
    #     {'city_code' : 41830, 'city_name' : '양평군'},
    # ]
    #
    # for cit in city :
    #     with db.cursor() as cursor :
    #         sql = """
    #                 insert City(city_code, city_name) values(%d, "%s")
    #               """%(cit['city_code'],cit['city_name'])
    #         cursor.execute(sql)
    # db.commit()



    # hos_dict = {}; subject = []
    # for item in jsonObj :
    #     treat_split = str(item['TREAT_SBJECT_CONT_INFO']).split(', ')
    #     for i in treat_split :
    #         subject.append(i)
    # for item in jsonObj2 :
    #     treat_split = str(item['TREAT_SBJECT_CONT_INFO']).split(', ')


    # Subject table
    #     for i in treat_split :
    #         subject.append(i)
    # subject = remove_redundancy(subject)
    # for sub in subject :
    #     with db.cursor() as cursor :
    #         sql = """
    #                 insert Subject(과목명) value("%s")
    #               """%(sub)
    #         cursor.execute(sql)
    # db.commit()


    # with db.cursor() as cursor:
    # Hospital table
    # hos_dict['name'] = item['BIZPLC_NM']
    # hos_dict['type'] = item['BIZCOND_DIV_NM_INFO']
    # hos_dict['cnt_nur'] = item['MEDSTAF_CNT']
    # hos_dict['tel'] = item['LOCPLC_FACLT_TELNO']
    # li = item['LICENSG_DE']
    # date = li[:4] + '-' + li[4:6] + '-' + li[-2:]
    # hos_dict['license'] = date
    #         sql = """
    #               insert Hospital(이름,Type,의료인_수,전화번호,인허가일자) values("%s","%s","%s","%s","%s")
    #               """%(hos_dict['name'],hos_dict['type'],hos_dict['cnt_nur'],hos_dict['tel'],hos_dict['license'])
    #         cursor.execute(sql)
    # db.commit()