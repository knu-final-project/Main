<<<<<<< HEAD
from flask import Flask,render_template,request,redirect
import pickle
from flask_cors import CORS, cross_origin
import argparse
import io
from PIL import Image

import torch
SURVEY_URL = "/survey"
DETECTION_URL = "/predict"

# from keras import models
file=open('data\DI2_DG.pkl','rb')
clf=pickle.load(file)

file.close()

app=Flask(__name__)

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
=======
from flask import Flask,render_template,request,redirect
import pickle
from flask_cors import CORS, cross_origin
import argparse
import io
from PIL import Image

import torch
SURVEY_URL = "/survey"
DETECTION_URL = "/predict"

# from keras import models
file=open('data\DI2_DG.pkl','rb')
clf=pickle.load(file)

file.close()

app=Flask(__name__)

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
>>>>>>> b21df5300f3803c89bf2962b2ecd93204d820791
