## 경로 변경 및 출력
# import os
# os.chdir('C:\Main\hyerim\data')
# print(os.getcwd())

## 데이터 불러오기
import pandas as pd
dis = pd.read_csv('hyerim\data\data_dis.csv',index_col=0)
#print(data)

### 질병에 따른 각 변수에 대한 사전
import pickle
with open('hyerim\data\dis_var.pkl', 'rb') as f:
    dis_var = pickle.load(f)

### 질병이름 사전
with open('hyerim\data\dis_name.pkl', 'rb') as f:
    dis_name = pickle.load(f)


#print('질병에 따른 각 변수에 대한 사전')
#print(dis_var)
#print('질병이름 사전')
#print(dis_name)



## 결과 프레임
result = pd.DataFrame(columns=['user_id','DI2_DG', 'DI3_DG', 'DI4_DG', 'DI5_DG', 'DM2_DG', 'DM3_DG', 'DM4_DG',
    'DJ2_DG', 'DJ4_DG', 'DJ6_DG', 'DJ8_DG', 'DI6_DG', 'DF2_DG', 'DL1_DG',
    'DE1_DG', 'DE2_DG', 'DH4_DG', 'DC1_DG', 'DC3_DG', 'DK8_DG'])
result

## 생활패턴 유사도
def model(test, err9 = False, err9value = 21):
    print(test)
    test['HE_BMI'] = 0
    test['HE_BMI'] = round((test['HE_WT'] / (test['HE_HT'] * 2))*100,1)
    test['TOTAL_SLP_WD'] = test['TOTAL_SLP_WD']*60

    if 'user_id' in test.columns:
        result.loc[0,'user_id'] = test.values[0][0]
        print(f"{test.values[0][0]}님과 각 질병 유병자들과의 생활패턴 유사도 결과입니다.\n")
        data = test.drop('user_id',axis=1)
    else:
        print("각 질병 유병자들과의 생활패턴 유사도 결과입니다.",'\n')
        data = test

    for i in range(0,len(dis.columns)-1):
        if not (err9 and dis.columns[i] == 'DJ4_DG'):
        ## 질병 머신러닝 모델
            with open(f'hyerim\data\{dis.columns[i]}.pkl', 'rb') as f:
                model = pickle.load(f)
                percent = round(model.predict_proba(data.iloc[[0]][dis_var[dis.columns[i]]])[0][1]*100,2)
            print(f'{dis_name[dis.columns[i]]} : {percent}%')
        else:
            percent = err9value
        
        result.loc[0,dis.columns[i]] = percent

    name = []
    for i in range(0,len(dis_name)):
        name.append(sorted(dis_name.items())[i][1])

    data = pd.DataFrame({'dis' : list(result.iloc[0,1:].sort_index().index),
    'percent': list(result.iloc[0,1:].sort_index()),
    'name': name})

    data['color'] = '0'

    for i in range(0,len(data)):
        if data['percent'][i] >90:
            data['color'][i] = '#ed023d'
        elif data['percent'][i] > 50:
            data['color'][i] = '#ed9f02'
        else:
            data['color'][i] = '#9ade08'

    data = data.sort_values(by='percent',ascending=False)
    print(result)

    return result, data
