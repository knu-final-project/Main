import glob
import pandas as pd
import time
import pymysql

"""
__init__(self) : google cloud platform에 있는 mysql DB에 접속 할 수 있습니다.

select_query(self, query) : 우리가 select query문을 작성하면 dataframe으로 결과를 return해줍니다.
                            query는 SQL의 SELECT 쿼리문을 작성해주세요.

label_to_meals(self, path, id="") : 저희가 객체탐지를 하기 위해 넣은 이미지에서 탐지한 사진을 기준으로
                    식단의 영양소 총합을 구해서 meals table에 넣어줍니다.
                    path은 detect에서 결과로 나온 "txt파일의 경로"를 말합니다. (저희 경로는 디폴트)
                    id는 저장할 id를 집어넣어주세요.
"""

class meals():
    def __init__(self):
        self.conn = pymysql.connect(user='root', passwd='1234', host='34.64.195.167', db='mydb129', charset='utf8')

    def select_query(self, query):
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        try:
            cur.execute(query)
            dic_result = cur.fetchall()
            result = pd.DataFrame(dic_result)
            return result
        except:
            print('select_query Error!')

    def label_to_meals(self, path="static\detect\exp\labels\image1.txt", id=""):
        # file_path = 'D:\Final_Project\Git_repositories\Main\static\detect\exp\labels'
        with open(path, 'r') as f:
            data = f.readlines()
        
        # Label num = class num
        label_num_list = []
        for a in data:
            label_num_list.append(int(a.split(' ')[0]))
        
        
        # Query 만들기
        # Select "요기" FROM "조기"
        cur = self.conn.cursor()
        try:
            # cur.execute("Select COLUMN_NAME From INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Food' and data_type = 'double precision' order by ordinal_position;") # postgresql
            cur.execute("Select COLUMN_NAME From INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Food' and data_type = 'float' order by ordinal_position;") # mysql
            fcolumns = cur.fetchall()
        except:
            print('M129 Query Make Error')

        ## "요기"
        label_list = list(set(label_num_list)) # list > set > list 를 통해 중복값을 제거 해줌.
        columns_query = ''
        for i in fcolumns:
            columns_query += 'sum(' + i[0] + '), '
        columns_query = columns_query.rstrip(', ')

        ## "조기"
        where_query = ''
        for i in label_list:
            where_query += 'class_num = ' + str(i) + " or "
        where_query = where_query.rstrip(' or ')

        query = 'SELECT ' + columns_query + ' FROM Food WHERE ' + where_query

        # 쿼리 실행
        cur=self.conn.cursor()
        try:
            cur.execute(query)
            score = cur.fetchall() # score = meals 영양소
        except:
            print('yogijogi Error!')

        # ID 기준 db insert
        now = time.strftime('%Y-%m-%d %H:%M:%S')

        valuestxt = "('" + id + "', '" + now + "'"
        for i in score[0]:
            valuestxt += ", "
            valuestxt += str(i)
        valuestxt += ');'

        insertquery = 'INSERT INTO meals VALUES ' + valuestxt

        cur=self.conn.cursor()
        try:
            cur.execute(insertquery)
            self.conn.commit()
        except:
            print('insertquery Error!')
        
    def db_close(self):
        self.conn.close()

    def dis_results_input(self, dis_results_dic, id):
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        try:
            cur.execute(f'SELECT cnt FROM dis_results WHERE user_id = {id} ORDER BY cnt DESC;')
            dic_result = cur.fetchall()
            result = pd.DataFrame(dic_result)
        except:
            print('select_query Error!')
        
        cur = self.conn.cursor()
        try:
            cnt = 0 # test : result['cnt'][0] error
            cur.execute(f"INSERT INTO dis_results VALUES (\
                {dis_results_dic['DI2_DG']},\
                {dis_results_dic['DI3_DG']},\
                {dis_results_dic['DI4_DG']},\
                {dis_results_dic['DI5_DG']},\
                {dis_results_dic['DM2_DG']},\
                {dis_results_dic['DM3_DG']},\
                {dis_results_dic['DM4_DG']},\
                {dis_results_dic['DJ2_DG']},\
                {dis_results_dic['DJ4_DG']},\
                {dis_results_dic['DJ6_DG']},\
                {dis_results_dic['DJ8_DG']},\
                {dis_results_dic['DI6_DG']},\
                {dis_results_dic['DF2_DG']},\
                {dis_results_dic['DL1_DG']},\
                {dis_results_dic['DE1_DG']},\
                {dis_results_dic['DE2_DG']},\
                {dis_results_dic['DH4_DG']},\
                {dis_results_dic['DC1_DG']},\
                {dis_results_dic['DC3_DG']},\
                {dis_results_dic['DK8_DG']},\
                {id},\
                {cnt+1}\
                ")
            self.conn.commit()
        except pymysql.ProgrammingError:
            cnt = 0
            cur.execute(f"INSERT INTO dis_results VALUES (\
                {dis_results_dic['DI2_DG']},\
                {dis_results_dic['DI3_DG']},\
                {dis_results_dic['DI4_DG']},\
                {dis_results_dic['DI5_DG']},\
                {dis_results_dic['DM2_DG']},\
                {dis_results_dic['DM3_DG']},\
                {dis_results_dic['DM4_DG']},\
                {dis_results_dic['DJ2_DG']},\
                {dis_results_dic['DJ4_DG']},\
                {dis_results_dic['DJ6_DG']},\
                {dis_results_dic['DJ8_DG']},\
                {dis_results_dic['DI6_DG']},\
                {dis_results_dic['DF2_DG']},\
                {dis_results_dic['DL1_DG']},\
                {dis_results_dic['DE1_DG']},\
                {dis_results_dic['DE2_DG']},\
                {dis_results_dic['DH4_DG']},\
                {dis_results_dic['DC1_DG']},\
                {dis_results_dic['DC3_DG']},\
                {dis_results_dic['DK8_DG']},\
                {id},\
                {cnt+1}\
                ")
            self.conn.commit()
    
    def dis_food(self, id, conf=0.5, recent = 1):
        # id에 맞는 최근 질병탐지 기록 가져오기 (result_row)
        # recent = 최근 기준 첫번째 1 / 두번째 2 ...
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        try:
            cur.execute(f'SELECT * FROM dis_results WHERE user_id = {id} ORDER BY cnt DESC;')
            dic_result = cur.fetchall()
            result = pd.DataFrame(dic_result)
        except:
            print('select_query Error!')
            return []
        
        if len(result) != 0:
            try:
                result_row = result.loc[recent-1]
            except KeyError:
                return []
            
        # 질병기록 중 conf 보다 넘는 확률의 질병들 추출 (columns_name)
        columns_name = []
        cur = self.conn.cursor()
        cur.execute("Select COLUMN_NAME From INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'dis_results' and data_type = 'float' order by ordinal_position;")
        fcolumns = cur.fetchall()
        
        for i in fcolumns:
            if result_row[i[0]] > conf:
                columns_name.append(i[0])
        
        # 질병 기록 기준으로 Bad food 를 찾기.
        select_query = 'SELECT * FROM disease'
        if len(columns_name) != 0:
            select_query += ' WHERE '
            for column in columns_name:
                select_query += f'disease_code = "{column}" or '
            select_query = select_query.rstrip(' or ')

        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(select_query)
        dis_table = cur.fetchall()
        dis_df = pd.DataFrame(dis_table)
        bad_food = dis_df['bad_food']
        bad_food_list = []
        for food_name in bad_food:
            food_name2 = food_name.replace('/r','')
            food_name_li = food_name2.split('_')
            bad_food_list += food_name_li
        
        bad_food_list = list(set(bad_food_list))

        bad_food_list_int = []
        for bad_food_str in bad_food_list:
            bad_food_list_int.append(int(bad_food_str))
        
        return bad_food_list_int



        

        


