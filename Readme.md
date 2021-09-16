# 기능정리
* 병원정보 제공
    * 전체정보
    * 진료과목
    * 주소
    * 전화번호
    * 병원 종
    * 총 의료인 수
* 조건에 맞는 병원 리스트 출력
    * 지역에 해당되는 병원 
    * 지역 + 진료과목
    * 지역 + 병원 종
* 추가기능
    * 지역별 5대질병에 대한 경고도 및 대응법(실시간성)
    * corona 현황?(실시간성)
    * 네비게이션
    
# 시나리오
* 시나리오 1  (이상적)
C - 안녕하세요 저는 경기도 지역별 병원정보 알리미입니다!  
C  - 도움이 필요하시면 도움을 불러주세요!  
U - 의도4 도움말~  
C - 도움말 출력  
U - 김포시 병원 리스트!  (2)  
C - 병원리스트 출력  
C - 질병경고도 출력
U - 고려병원 전체정보 알려줘! OR 고려벙원 진료과목! OR 고려병원 위치알려줘!  (1)
C - 조건에 맞는 정보출력 및 길찾기(위치) 시 네비게이션기능 연결  

* 시나리오 2 (다이렉트)
C - 안녕하세요 저는 경기도 지역별 병원정보 알리미입니다!  
C  - 도움이 필요하시면 도움을 불러주세요!  
U - 의도4 도움말~  
C - 도움말 출력  
U - 김포시 고려병원 위치 알려주세요!
C - 위치출력 AND 네비게이션 링크  
OR  
U - 김포시 이비인후과 병원 알려줘  
C - 조건에 맞는 병원 리스트출력  
U - 고려병원 정보!  
C - 정보출력

# 의도
class|의도명
---|---|
0| 인사
1| 병원정보 출력
2| 병원 리스트 출력
3| 도움말
4| 코로나 현황

# 개체명
**B_Hospital** : 병원<br/>
**B_Location** : 주소<br/>
**B_City** : 도시<br/>
**B_S_C** : 동<br/>
B_Tel : 전화번호<br/>
B_Subject : 진료과목<br/>
B_Treat : 진료과목<br/>
B_Type : 병원 종

# API 활용 및 PK
**dissCd**  

질병코드|질병명
---|---|
1|감기
2|눈병
3|식중독
4|천식
5|피부염

**risk**

위험도|위험도명
---|---|
1|관심
2|주의
3|경고
4|위험

**znCd**
41 - 경기 

**lowrnkZnCd** 

code|city
---|---|
41111|수원시
41131|성남시
41150|의정부시
41171|안양시
41190|부천시
41210|광명시
41220|평택시
41250|동두천시
41271|안산시
41281|고양시
41290|과천시
41310|구리시
41360|남양주시
41370|오산시
41390|시흥시
41410|군포시
41430|의왕시
41450|하남시
41461|용인시
41480|파주시
41500|이천시
41550|안성시
41570|김포시
41590|화성시
41610|광주시
41630|양주시
41650|포천시
41670|여주시
41800|연천군
41820|가평군
41830|양평군

# 패치노트
1. 같은이름의 병원이름
2. FindAnswer 구현
3. 병원검색 시 운영중 / 폐쇄 확인
4. 버튼식 구현가능한지
5. FindAnswer, 다른의도들 다되게 수정필요.

<>
~~08.28 - 시나리오, 틀 작업.~~  
~~08.28 - max_seq_len = 12 설정~~  
~~08.29 - 의도 2개 새로 학습 (도움말, 코로나현황)~~  
~~08.30 - 개체명인식 새로 학습. ner 학습데이터 추가, 테스트완료~~  
~~08.31 API 활용신청 및 활용~~  
~~08.31 셀레니움 url띄우기까지만~~  
~~09.01 intent, ner Test~~  
~~09.01 완전히 동시에는 구동이 안되지만 어느정도 텀을 두고 가능~~    
~~09.01 db 설계 작동~~  
~~09.04 db 작동법, 테이블 설계, insert data(1)~~  
~~09.05 Hospital, city, subject insert data~~  
~~09.06 data insert~~  
~~09.07 DB dataa insert complete~~  
~~09.13 DB, 엔진 연동~~  
~~09.15 구름, db, 카카오 연동 확인~~  
~~09.17 db 연동 sql문 업데이트, intent{정보}~~  