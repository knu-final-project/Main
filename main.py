from tracemalloc import start
from flask import Flask,render_template,request,redirect
import pickle
from flask_cors import CORS, cross_origin
import argparse
import io
from PIL import Image
import torch

from py_modules import prediction_var



SURVEY_URL = "/survey"
DETECTION_URL = "/predict"

# from keras import models
file=open('data\DI2_DG.pkl','rb')
clf=pickle.load(file)

file.close()

app=Flask(__name__)
start_program = prediction_var.hello_world

cors = CORS(app)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response


@app.route(SURVEY_URL,methods=['GET','POST'])

def hello_world():
    if request.method == 'POST':
        mydict=request.form
        #mydict에서 문항 다 입력하고 거기서 
        LQ_3EQL = int(mydict['LQ_3EQL'])
        N_MUFA = int(mydict['N_MUFA'])
        TOTAL_SLP_WD = int(mydict['TOTAL_SLP_WD'])
        HE_BMI = int(mydict['HE_BMI'])
        N_PHOS = int(mydict['N_PHOS'])
        BD1_11 = int(mydict['BD1_11'])
        HE_WT = int(mydict['HE_WT'])
        BP1 = int(mydict['BP1'])
        N_FAT = int(mydict['N_FAT'])
        BH1 = int(mydict['BH1'])
        AGE = int(mydict['AGE'])
        N_CAROT = int(mydict['N_CAROT'])
        BS13 = int(mydict['BS13'])
        N_INTK = int(mydict['N_INTK'])
        N_EN = int(mydict['N_EN'])
        LQ_5EQL = int(mydict['LQ_5EQL'])
        BE3_85 = int(mydict['BE3_85'])
        N_WATER = int(mydict['N_WATER'])
        HE_HT = int(mydict['HE_HT'])
        N_CHOL = int(mydict['N_CHOL'])
        N_NA = int(mydict['N_NA'])
        N_PROT = int(mydict['N_PROT'])
        SEX = int(mydict['SEX'])
        BP7 = int(mydict['BP7'])
        LQ_2EQL = int(mydict['LQ_2EQL'])
        HE_DBP = int(mydict['HE_DBP'])
        LQ_1EQL = int(mydict['LQ_1EQL'])
        BE3_81 = int(mydict['BE3_81'])
        N_SFA = int(mydict['N_SFA'])
        ID = int(mydict['ID'])
        HE_RPLS = int(mydict['HE_RPLS'])
        N_SUGAR = int(mydict['N_SUGAR'])
        SM_PRESNT = int(mydict['SM_PRESNT'])
        L_BR_FQ = int(mydict['L_BR_FQ'])
        HE_FH = int(mydict['HE_FH'])
        LQ_4EQL = int(mydict['LQ_4EQL'])
        MH_STRESS = int(mydict['MH_STRESS'])
        LQ4_00 = int(mydict['LQ4_00'])

        DI2_DG_LIST = [SEX, HE_FH, HE_BMI,BH1,AGE,HE_HT,BD1_11,BP1,LQ_4EQL]
        DI3_DG_LIST = [LQ_3EQL,LQ_1EQL,LQ_2EQL,HE_RPLS,LQ_4EQL,AGE,LQ4_00,N_PHOS,N_PROT]
        DI4_DG_LIST = [HE_RPLS,HE_WT,HE_DBP,HE_DBP,LQ_3EQL,SEX,HE_BMI,AGE,HE_HT,HE_FH]
        DI5_DG_LIST = [SEX,AGE,HE_DBP,HE_DBP,HE_HT,HE_WT,BS13,HE_RPLS,BE3_81]
        DM2_DG_LIST = [SEX,HE_HT,LQ_4EQL,LQ_1EQL,LQ_3EQL,HE_BMI,BD1_11,LQ4_00,N_EN,LQ_5EQL]
        DM3_DG_LIST = [SEX, LQ_4EQL,HE_HT,LQ_1EQL,MH_STRESS,N_NA,HE_WT,LQ_3EQL,N_EN,LQ4_00]
        DM4_DG_LIST = [SEX,HE_HT,HE_WT,BD1_11,N_EN,LQ_4EQL,N_PROT,N_PHOS,N_NA]
        DJ2_DG_LIST = [HE_BMI,HE_HT,SEX,AGE,BE3_85,HE_FH,N_CHOL,N_MUFA,N_FAT,L_BR_FQ]
        DJ4_DG_LIST = [LQ_4EQL, LQ_3EQL,LQ_5EQL,LQ_1EQL,AGE,MH_STRESS,BD1_11,HE_HT,N_INTK]
        DJ6_DG_LIST = [BP1,LQ_5EQL,LQ_4EQL,N_CAROT,BE3_81,BH1,BP7,N_SUGAR]
        DJ8_DG_LIST = [BP7,AGE,BP1,SM_PRESNT,MH_STRESS,N_CAROT,N_WATER,HE_FH]
        DI6_DG_LIST = [HE_RPLS,LQ_3EQL,HE_DBP,HE_DBP,LQ_4EQL,HE_WT,LQ4_00,HE_BMI,LQ_5EQL,AGE]
        DF2_DG_LIST = [BP7,LQ_5EQL,BP1,SEX,MH_STRESS,LQ4_00,LQ_4EQL,HE_HT,BD1_11,LQ_1EQL]
        DL1_DG_LIST = [LQ_5EQL, LQ_4EQL, BP7, LQ_3EQL, BS13, BE3_85, BP1]
        DE1_DG_LIST = [HE_DBP, HE_DBP, HE_BMI, HE_WT, HE_FH, LQ_2EQL, LQ_1EQL, N_SUGAR, LQ_3EQL, N_SFA]
        DE2_DG_LIST = [SEX,AGE,HE_FH,BP1,BD1_11,SM_PRESNT,HE_HT,MH_STRESS,LQ_4EQL,HE_WT]
        DH4_DG_LIST = [LQ4_00,LQ_3EQL,BP1,BP7,MH_STRESS,LQ_4EQL,HE_FH,TOTAL_SLP_WD]
        DC1_DG_LIST = [HE_BMI,SEX,HE_HT,BH1,AGE,LQ_4EQL,HE_WT,HE_DBP,HE_DBP,L_BR_FQ]
        DC3_DG_LIST = [SEX, BH1, HE_HT, N_MUFA, N_SFA, N_FAT, N_CHOL]
        DK8_DG_LIST = [AGE,N_WATER,HE_HT,L_BR_FQ,SM_PRESNT,N_SUGAR,TOTAL_SLP_WD,N_INTK]

 
        #input_feature=[100,1,45,1,1,0]
        
        infprob=clf.predict_proba([DI2_DG_LIST])[0][1]
        
        return render_template('result.html',inf=(round(infprob*10**11,2)), inf2='2', inf3 = '3', inf4 = '4')
   
    return render_template('index.html')

@app.route(DETECTION_URL, methods=["GET","POST"])
def predict():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if not file:
            return

        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        results = model(img, size=640)

        # for debugging
        # data = results.pandas().xyxy[0].to_json(orient="records")
        # return data

        results.render()  # updates results.imgs with boxes and labels
        for img in results.imgs:
            img_base64 = Image.fromarray(img)
            img_base64.save("static/image0.jpg", format="JPEG")
        return redirect("static/image0.jpg")

    return render_template("detect.html")
    
if __name__ == '__main__'  :
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()

    model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True, force_reload=True, autoshape=True)  # force_reload = recache latest code
    model.eval()
    app.run(debug=True) 

