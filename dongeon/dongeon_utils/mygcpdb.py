import pandas as pd
import pymysql
import time

"""
conn_db(self, pw) : pw를 입력하면 google cloud platform에 있는 mysql DB에 접속 할 수 있습니다.
                    여기서 return되는 값을 항상 다음 함수들에 넣어주셔야 사용 하실 수 있습니다.

select_query(self, conn, query) : 우리가 select query문을 작성하면 dataframe으로 결과를 return해줍니다.
                    conn은 위 conn_db에서 return받은 변수를 넣어주시고,
                    query는 SQL의 SELECT 쿼리문을 작성해주세요.

label_to_meals(self, conn, label, id="") : 저희가 객체탐지를 하기 위해 넣은 이미지에서 탐지한 사진을 기준으로
                    식단의 영양소 총합을 구해서 meals table에 넣어줍니다.
                    conn은 위 conn_db에서 return받은 변수를 넣어주시고,
                    label은 detect에서 결과로 나온 txt파일을 말합니다.
                    id는 저장할 id를 집어넣어주세요.
                    return 값은 확인용으로 meals table의 모든 값을 dataframe으로 받습니다.
"""

# 1. DB에 연결
def conn_db(self, pw):
    try:
        conn = pymysql.connect(user='root', passwd=str(pw), host='34.64.136.121', db='mydb129', charset='utf8')
        print('===접속 성공===')
        return conn
    except pymysql.DatabaseError as db_err:
        print('접속 오류 !!')
        print(db_err)


# 2. Select Query (쿼리문을 입력 → DataFrame으로 return)
def select_query(self, conn, query):
    cur = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cur.execute(query)
        dic_result = cur.fetchall()
        result = pd.DataFrame(dic_result)
        return result
    except:
        print('select_query Error!')

# 3. label txt 파일을 입력 받아서 안에 있는 영양소를 기준으로 meals에 집어 넣어버리는 function
def label_to_meals(self, conn, label, id=""):
    cur = conn.cursor()
    
    # label은 파일 경로
    with open(label, 'r') as f:
        data = f.readlines()
    label_list = []
    for a in data:
        label_list.append(int(a.split(' ')[0]))    # label.txt에서 class num 만 추출

    
    # 아래는 label_list를 기준으로 총합 영양소를 찾아내는 QUERY
    ## Query를 짜보자
    ### 문자열 제외한 컬럼들
    cur=conn.cursor()
    try:
        cur.execute("Select COLUMN_NAME From INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Food' and data_type = 'float' order by ordinal_position;")
        fcolumns = cur.fetchall()
    except:
        print('Select COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE ~ !')

    ## 식단 (Sample 16, 8, 7 의 영양분을 다 합친 값을 구할 예정)
    ### SELECT "요기" FROM FOOD WHERE "조기"
    #### 요기
    label_list = list(set(label_list)) # 라벨리스트 > 집합 > 라벨리스트 를 통해 중복값을 제거 해줌.
    columns_query = ''
    for i in fcolumns:
        columns_query += 'sum(' + i[0] + '), '
    columns_query = columns_query.rstrip(', ')

    #### 조기
    where_query = ''
    for i in label_list:
        where_query += 'class_num = ' + str(i) + " or "
    where_query = where_query.rstrip(' or ')
    query = 'SELECT ' + columns_query + ' FROM Food WHERE ' + where_query   # Complete

    # 그래서 총합 영양소는? score에 저장
    cur=conn.cursor()
    try:
        cur.execute(query)
        score = cur.fetchall()
    except:
        print('score Error!')
    
    # meals table에 집어넣어보자
    now = time.strftime('%Y-%m-%d %H:%M:%S')

    valuestxt = "('" + id + "', '" + now + "'"
    for i in score[0]:
        valuestxt += ", "
        valuestxt += str(i)
    valuestxt += ');'

    insertquery = 'INSERT INTO meals VALUES ' + valuestxt

    cur=conn.cursor()
    try:
        cur.execute(insertquery)
        conn.commit()
    except:
        print('INSERT INTO meals Error!')

    # 결과값을 확인시켜주자
    cur=conn.cursor(pymysql.cursors.DictCursor)
    try:
        cur.execute("SELECT * FROM meals;")
        meals_check = cur.fetchall()
        meals_df = pd.DataFrame(meals_check)
        return meals_df
    except:
        print('Check Error!')

