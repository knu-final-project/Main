import pymysql

class Food():
    def __init__(self):
        pass

    def get_table(self):
        ret = []
        conn = pymysql.connect(user='root', passwd='1234', host='34.64.136.121', db='mydb129', charset='utf8')
        curs = conn.cursor()

        query = "SELECT * FROM Food;"
        curs.execute(query)
        rows = curs.fetchall()

        for e in rows:
            temp = {
                'class_num':e[0], 
                'food_name':e[1], 
                'serving_size':e[2], 
                'calorie_kJ':e[3], 
                'calorie_kcal':e[4], 
                'carbohydrate_g':e[5],
                'sugar_g':e[6],
                'protein_g':e[7],
                'fat_g':e[8],
                'saturated_fat_g':e[9],
                'polyunsaturated_fat_g':e[10],
                'unsaturated_fat_g':e[11],
                'cholesterol_mg':e[12],
                'dietary_fiber_g':e[13],
                'salt_mg':e[14],
                'potassium_mg':e[15]
            }
            ret.append(temp)
        
        conn.commit()
        conn.close()

        return ret
    
    if __name__ == '__main__':
        emplist = Food.get_table()