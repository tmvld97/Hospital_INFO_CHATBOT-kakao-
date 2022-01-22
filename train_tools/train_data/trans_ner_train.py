import requests
import xmltodict
import json
from konlpy.tag import Komoran



def remove_redundancy(list_A):  # list 중복제거 함수
    set_list = set(list_A)
    remove_list = list(set_list)
    return remove_list



url = "https://openapi.gg.go.kr/GgHosptlM?KEY=337b4bebd30e4d419b85a1ba8c9c26a2&pSize=1000"
url2 = "https://openapi.gg.go.kr/GgHosptlM?KEY=337b4bebd30e4d419b85a1ba8c9c26a2&pIndex=2&pSize=1000"
content = requests.get(url).content
content2 = requests.get(url2).content

dict = xmltodict.parse(content)
dict2 = xmltodict.parse(content2)

jsonString = json.dumps(dict['GgHosptlM']['row'], ensure_ascii=False)  # <GgHosptlM> 태그의 <row> 정보
jsonString2 = json.dumps(dict2['GgHosptlM']['row'], ensure_ascii=False)

jsonObj = json.loads(jsonString)
jsonObj2 = json.loads(jsonString2)

hospital = [];
subject = [];
location = [];
tel = [];
city = [];
s_c = [];
type = ['요양병원', '치과병원', '한방병원', '종합병원'];
treat = []
letter = []

#
for tag in jsonObj:
    hospital.append(tag['BIZPLC_NM'])
    city.append(tag['SIGUN_NM'])

    split_s_c = str(tag['REFINE_LOTNO_ADDR']).split(' ')
    treat_split = str(tag['TREAT_SBJECT_CONT_INFO']).split(', ')
    for i in treat_split:
        treat.append(i)
    if len(split_s_c) >= 3:
        s_c.append(split_s_c[2])

for tag2 in jsonObj2:
    hospital.append(tag2['BIZPLC_NM'])
    city.append(tag2['SIGUN_NM'])
    split_s_c = str(tag2['REFINE_LOTNO_ADDR']).split(' ')
    treat_split = str(tag2['TREAT_SBJECT_CONT_INFO']).split(', ')
    for i in treat_split:
        treat.append(i)
    if len(split_s_c) >= 3:
        s_c.append(split_s_c[2])

hospital.append('해암요양병원')
hospital.append('청구요양병원')
hospital.append('부천당당양한방병원')
hospital.append('서울와이즈재활요양병원')

# hospital.append('의료법인오엠씨의료재단 중앙병원')
city = remove_redundancy(city)
s_c = remove_redundancy(s_c)
treat = remove_redundancy(treat)
city2 = []
for item in city:
    city2.append(item[:-1])


#
#
# f = open('new_test.txt', 'r',encoding= 'utf-8')
f = open('add_trans_2.txt', 'r', encoding='utf-8')
# f2 = open('test_ner.txt','r',encoding= 'utf-8')
f3 = open('add_new_NER_2.txt', 'a', encoding='utf-8')

count = 0;
line_counter = 0
for item in f:
    #     if item[-2] == '1' or item[-1] == '1':  # 43까지는 의도클래스(0)에 해당.
    #         line_counter += 1
            letter.append(item[5:-3])  # indexing

count = 0
komoran = Komoran(userdic='../../utils/user_dic.txt')
for item in letter:
    count += 1
    # print(';' + item)
    f3.write('; ' + item + '\n')
    morphs = komoran.pos(item)  # 형태소 분석기
    index = 0
    fixed = ''
    count = 0
    for token in morphs:
        if  token[0] in city2 :  # token[0] : 토큰된 단어 token[1] : 토크나이징 된 토큰의 형태소
            cit = '<' + token[0] + ':City>'
            fixed = item.replace(token[0]+'에 있는', cit + '에 있는')

        if token[0] in hospital  : # token[0] : 토큰된 단어 token[1] : 토크나이징 된 토큰의 형태소
            hos = '<' + token[0] + ':Hospital>'
            fixed = fixed.replace(token[0], hos)

        elif token[0] in subject :
            sub = '<' + token[0] + ':Subject>'
            fixed = fixed.replace(token[0], sub)
        elif token[0] in location :
            loc = '<' + token[0] + ':Location>'
            fixed = fixed.replace(token[0], loc)
        elif token[0] in tel :
            t = '<' + token[0] + ':Tel>'
            fixed = fixed.replace(token[0], t)

    if fixed == '' : print(item, fixed)
    else : f3.write('$'+fixed+'\n')
    for token2 in morphs :
        index += 1
        if token2[0] in hospital :
                # print('{0}\t{1}\t{2} B_Hospital'.format(index, token2[0], token2[1]))
            f3.write('{0}\t{1}\t{2} B_Hospital'.format(index, token2[0], token2[1]))
        elif token2[0] in subject :
                # print('{0}\t{1}\t{2} B_Subject'.format(index, token2[0], token2[1]))
            f3.write('{0}\t{1}\t{2} B_Subject'.format(index, token2[0], token2[1]))
        elif token2[0] in location :
               # print('{0}\t{1}\t{2} B_Location'.format(index, token2[0], token2[1]))
            f3.write('{0}\t{1}\t{2} B_Location'.format(index, token2[0], token2[1]))
        elif token2[0] in tel :
                #print('{0}\t{1}\t{2} B_Tel'.format(index, token2[0], token2[1]))
            f3.write('{0}\t{1}\t{2} B_Tel'.format(index, token2[0], token2[1]))
        elif token2[0] in city2:  # token[0] : 토큰된 단어 token[1] : 토크나이징 된 토큰의 형태소
                f3.write('{0}\t{1}\t{2} B_City'.format(index, token2[0], token2[1]))
        else :
            f3.write('{0}\t{1}\t{2} O'.format(index, token2[0], token2[1]))
        f3.write('\n')
    f3.write('\n')

    #     if token[0] in city:  # token[0] : 토큰된 단어 token[1] : 토크나이징 된 토큰의 형태소
    #         hos = '<' + token[0] + ':City>'
    #         fixed = item.replace(token[0], hos)
    #     elif token[0] in s_c:
    #         sc = '<' + token[0] + ':S_c>'
    #         if token[0] == '정왕동' or token[0] == '신천동':
    #             fixed = item.replace(token[0], sc)
    #         else:
    #             fixed = fixed.replace(token[0], sc)
    #     elif token[0] in treat:
    #         tr = '<' + token[0] + ':Treat>'
    #         fixed = fixed.replace(token[0], tr)
    # if fixed == '':
    #     print("에러", item, fixed)
    # else:
    #     f3.write('$' + fixed + '\n')
    # #
    # for token2 in morphs:
    #     index += 1
    #     if token2[0] in city:  # token[0] : 토큰된 단어 token[1] : 토크나이징 된 토큰의 형태소
    #         f3.write('{0}\t{1}\t{2} B_City'.format(index, token2[0], token2[1]))
    #     elif token2[0] in s_c:
    #         f3.write('{0}\t{1}\t{2} B_S_c'.format(index, token2[0], token2[1]))
    #     elif token2[0] in treat:
    #         f3.write('{0}\t{1}\t{2} B_Treat'.format(index, token2[0], token2[1]))
    #     else:
    #         f3.write('{0}\t{1}\t{2} O'.format(index, token2[0], token2[1]))
    #     f3.write('\n')
    # f3.write('\n')
    # print()
f.close()
f3.close()



