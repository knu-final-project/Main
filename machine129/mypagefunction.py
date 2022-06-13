import pandas as pd
import time
import pymysql

class db_class():
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
    
    def db_close(self):
        self.conn.close()

    def over_disease(self, id, conf=50, percent=False):
        df = self.select_query(f'SELECT * FROM dis_results WHERE user_id = {id};')
        df = df.sort_values('cnt', ascending=False)
        df = df.reset_index(drop=False, inplace=False).head(1)
        df_result = df.iloc[:,1:21]
        #오름차순 후 1row, 20개 질병 column추출 #
        df_result = df_result.transpose()
        df_dict = df_result.to_dict()
        df_dict = df_dict[0]
        
        red_list =[]
        red_percent = []
        for i in df_dict:
            a = df_dict[i] # i는 코드 a는 확률
            if a > conf:
                red_list.append(i) # conf 넘는 질병 코드
                red_percent.append([i, a])

        red_name_list = [] # 50 넘는 질병명
        red_name_percent_list = []
        for num, a in enumerate(red_list):
            df_disname = self.select_query(f"SELECT disease_name FROM disease WHERE disease_code = '{a}';")
            dis_kor = df_disname['disease_name'][0]
            red_name_list.append(dis_kor)

            if red_percent[num][0] == a:
                pc = red_percent[num][1]
                red_name_percent_list.append([dis_kor, pc])

        if percent:
            return red_name_percent_list
        else:
            return red_name_list
            

