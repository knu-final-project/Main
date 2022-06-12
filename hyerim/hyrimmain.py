from flask import Flask, render_template, request
import model_data # 데이터가 있는 곳
import pandas as pd
import numpy as np
import test

# 앱 생성
app = Flask(__name__)

# url 라우터
@app.route('/')
def survey():
    return render_template('질병예측3.html')

@app.route('/survey', methods= ['POST', 'GET']) 
def result():
    mydict=request.form
    if request.method == 'POST':
        survey_data = pd.DataFrame({
        'LQ_3EQL' : float(mydict['LQ_3EQL']),
        'N_MUFA' : float(mydict['N_MUFA']),
        'TOTAL_SLP_WD' : float(mydict['TOTAL_SLP_WD']),
        'N_PHOS' : float(mydict['N_PHOS']),
        'BD1_11' : float(mydict['BD1_11']),
        'HE_WT' : float(mydict['HE_WT']),
        'BP1' : float(mydict['BP1']),
        'N_FAT' : float(mydict['N_FAT']),
        'BH1' : float(mydict['BH1']),
        'AGE' : float(request.form['AGE']),
        'N_CAROT' : float(mydict['N_CAROT']),
        'BS13' : float(mydict['BS13']),
        'N_INTK' : float(mydict['N_INTK']),
        'N_EN' : float(mydict['N_EN']),
        'LQ_5EQL' : float(mydict['LQ_5EQL']),
        'BE3_85' : float(mydict['BE3_85']),
        'N_WATER' : float(mydict['N_WATER']),
        'HE_HT' : float(mydict['HE_HT']),
        'N_CHOL' : float(mydict['N_CHOL']),
        'N_NA' : float(mydict['N_NA']),
        'N_PROT' : float(mydict['N_PROT']),
        'SEX' : int(request.form['SEX']), #request.form['SEX']
        'BP7' : float(mydict['BP7']),
        'LQ_2EQL' : float(mydict['LQ_2EQL']),
        'HE_DBP' : float(mydict['HE_DBP']),
        'LQ_1EQL' : float(mydict['LQ_1EQL']),
        'BE3_81' : float(mydict['BE3_81']),
        'N_SFA' : float(mydict['N_SFA']),
        'HE_RPLS' : float(mydict['HE_RPLS']),
        'N_SUGAR' : float(mydict['N_SUGAR']),
        'SM_PRESNT' : float(mydict['SM_PRESNT']),
        'L_BR_FQ' : float(mydict['L_BR_FQ']),
        'HE_FH' : float(mydict['HE_FH']),
        'LQ_4EQL' : float(mydict['LQ_4EQL']),
        'MH_STRESS' : float(mydict['MH_STRESS']),
        'LQ4_00' : float(mydict['LQ4_00'])
        }, index=np.arange(1))


        #result = request.form
    result, data = model_data.model(survey_data)
    print(data)
    ag = pd.read_csv('data_ag.csv', index_col=0)

    # result : 생활패턴 유사도 수치!! DB에 연결하면 될 것 같습니다:)


    return render_template('detect_result.html', data=data, ag = ag, survey_data = survey_data)


# 메인 영역
if __name__ == "__main__":
    app.run(debug=True, port=9999)
 