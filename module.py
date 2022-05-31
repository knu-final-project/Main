<<<<<<< HEAD
from flask import Flask,render_template,request
import pickle

def hello_world():
    if request.method == 'POST':
        mydict=request.form
        #mydict에서 문항 다 입력하고 거기서 

        HE_BMI = int(mydict['HE_BMI'])
        BD1_11 = int(mydict['BD1_11'])
        BP1 = int(mydict['BP1'])
        BH1 = int(mydict['BH1'])
        AGE = int(mydict['AGE'])
        HE_HT = int(mydict['HE_HT'])
        SEX = int(mydict['SEX'])
        HE_FH = int(mydict['HE_FH'])
        LQ_4EQL = int(mydict['LQ_4EQL'])

        DI2_DG_LIST = [SEX, HE_FH, HE_BMI,BH1,AGE,HE_HT,BD1_11,BP1,LQ_4EQL]

 
        #input_feature=[100,1,45,1,1,0]
        
        infprob=clf.predict_proba([DI2_DG_LIST])[0][1]
        return render_template('result.html',inf=(round(infprob*10**11,2)))
   
=======
from flask import Flask,render_template,request
import pickle

def hello_world():
    if request.method == 'POST':
        mydict=request.form
        #mydict에서 문항 다 입력하고 거기서 

        HE_BMI = int(mydict['HE_BMI'])
        BD1_11 = int(mydict['BD1_11'])
        BP1 = int(mydict['BP1'])
        BH1 = int(mydict['BH1'])
        AGE = int(mydict['AGE'])
        HE_HT = int(mydict['HE_HT'])
        SEX = int(mydict['SEX'])
        HE_FH = int(mydict['HE_FH'])
        LQ_4EQL = int(mydict['LQ_4EQL'])

        DI2_DG_LIST = [SEX, HE_FH, HE_BMI,BH1,AGE,HE_HT,BD1_11,BP1,LQ_4EQL]

 
        #input_feature=[100,1,45,1,1,0]
        
        infprob=clf.predict_proba([DI2_DG_LIST])[0][1]
        return render_template('result.html',inf=(round(infprob*10**11,2)))
   
>>>>>>> b21df5300f3803c89bf2962b2ecd93204d820791
    return render_template('index.html')