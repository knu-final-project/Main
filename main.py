from flask import Flask,render_template,request,redirect,session,url_for
import pickle
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import argparse
import io
from PIL import Image
import json
from instagram import getfollowedby, getname
from datetime import timedelta



import torch
HOME_URL = "/"
SURVEY_URL = "/survey"
DETECTION_URL = "/predict"
# from keras import models
file=open('data\models\DI2_DG.pkl','rb')
clf1=pickle.load(file)
file.close()

file = open('data\models\DI3_DG.pkl','rb')
clf2 = pickle.load(file)
file.close()

file = open('data\models\DI4_DG.pkl','rb')
clf3 = pickle.load(file)
file.close()

file = open('data\models\DI5_DG.pkl','rb')
clf4 = pickle.load(file)
file.close()

file = open('data\models\DM2_DG.pkl','rb')
clf5 = pickle.load(file)
file.close()

file = open('data\models\DM3_DG.pkl','rb')
clf6 = pickle.load(file)
file.close()

file = open('data\models\DM4_DG.pkl','rb')
clf7 = pickle.load(file)
file.close()

file = open('data\models\DJ2_DG.pkl','rb')
clf8 = pickle.load(file)
file.close()

file = open('data\models\DJ4_DG.pkl','rb')
clf9 = pickle.load(file)
file.close()

file = open('data\models\DJ6_DG.pkl','rb')
clf10 = pickle.load(file)
file.close()

file = open('data\models\DJ8_DG.pkl','rb')
clf11 = pickle.load(file)
file.close()

file = open('data\models\DI6_DG.pkl','rb')
clf12 = pickle.load(file)
file.close()

file = open('data\models\DF2_DG.pkl','rb')
clf13 = pickle.load(file)
file.close()

file = open('data\models\DL1_DG.pkl','rb')
clf14 = pickle.load(file)
file.close()

file = open('data\models\DE1_DG.pkl','rb')
clf15 = pickle.load(file)
file.close()

file = open('data\models\DE2_DG.pkl','rb')
clf16 = pickle.load(file)
file.close()

file = open('data\models\DH4_DG.pkl','rb')
clf17 = pickle.load(file)
file.close()

file = open('data\models\DC1_DG.pkl','rb')
clf18 = pickle.load(file)
file.close()

file = open('data\models\DC3_DG.pkl','rb')
clf19 = pickle.load(file)
file.close()

file = open('data\models\DK8_DG.pkl','rb')
clf20 = pickle.load(file)
file.close()

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=1) # 로그인 지속시간을 정합니다. 현재 1분

db = SQLAlchemy(app)
cors = CORS(app)

class User(db.Model):
    """ Create user table"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    def __init__(self, username, password):
        self.username = username
        self.password = password

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response


@app.route('/',methods=['GET','POST'])
def home():
    """ Session control"""
    if not session.get('logged_in'):
        return render_template('home.html')
    else:
        if request.method == 'POST':
            username = getname(request.form['username'])
            return render_template('home.html', data=getfollowedby(username))
        return render_template('home.html')
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login Form"""
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        passw = request.form['password']
        try:
            data = User.query.filter_by(username=name, password=passw).first()
            if data is not None:
                session['logged_in'] = True
                return redirect(url_for('home'))
            else:
                return 'Dont Login'
        except:
            return "Dont Login"
 
 
@app.route('/register/', methods=['GET', 'POST'])
def register():
    """Register Form"""
    if request.method == 'POST':
        new_user = User(username=request.form['username'], password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
    return render_template('register.html')
     
 
@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('home'))
 
 
@app.route(SURVEY_URL,methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        mydict=request.form
        #mydict에서 문항 다 입력하고 거기서 

        LQ_3EQL = float(mydict['LQ_3EQL'])
        N_MUFA = float(mydict['N_MUFA'])
        TOTAL_SLP_WD = float(mydict['TOTAL_SLP_WD'])
        HE_BMI = float(mydict['HE_BMI'])
        N_PHOS = float(mydict['N_PHOS'])
        BD1_11 = float(mydict['BD1_11'])
        HE_WT = float(mydict['HE_WT'])
        BP1 = float(mydict['BP1'])
        N_FAT = float(mydict['N_FAT'])
        BH1 = float(mydict['BH1'])
        AGE = float(mydict['AGE'])
        N_CAROT = float(mydict['N_CAROT'])
        BS13 = float(mydict['BS13'])
        N_INTK = float(mydict['N_INTK'])
        N_EN = float(mydict['N_EN'])
        LQ_5EQL = float(mydict['LQ_5EQL'])
        BE3_85 = float(mydict['BE3_85'])
        N_WATER = float(mydict['N_WATER'])
        HE_HT = float(mydict['HE_HT'])
        N_CHOL = float(mydict['N_CHOL'])
        N_NA = float(mydict['N_NA'])
        N_PROT = float(mydict['N_PROT'])
        SEX = int(mydict['SEX'])
        BP7 = float(mydict['BP7'])
        LQ_2EQL = float(mydict['LQ_2EQL'])
        HE_DBP = float(mydict['HE_DBP'])
        LQ_1EQL = float(mydict['LQ_1EQL'])
        BE3_81 = float(mydict['BE3_81'])
        N_SFA = float(mydict['N_SFA'])
        HE_RPLS = float(mydict['HE_RPLS'])
        N_SUGAR = float(mydict['N_SUGAR'])
        SM_PRESNT = float(mydict['SM_PRESNT'])
        L_BR_FQ = float(mydict['L_BR_FQ'])
        HE_FH = float(mydict['HE_FH'])
        LQ_4EQL = float(mydict['LQ_4EQL'])
        MH_STRESS = float(mydict['MH_STRESS'])
        LQ4_00 = float(mydict['LQ4_00'])


        
        DI2_DG_LIST = [SEX, HE_FH, HE_BMI,BH1,AGE,HE_HT,BD1_11,BP1,LQ_4EQL]
        DI3_DG_LIST = [LQ_3EQL,LQ_1EQL,LQ_2EQL,HE_RPLS,LQ_4EQL,AGE,LQ4_00,N_PHOS,N_PROT]
        DI4_DG_LIST = [HE_RPLS,HE_WT,HE_DBP,LQ_3EQL,SEX,HE_BMI,AGE,HE_HT,HE_FH,BE3_81]
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
        
        
        infprob1 = clf1.predict_proba([DI2_DG_LIST])[0][1]
        infprob2 = clf2.predict_proba([DI3_DG_LIST])[0][1]
        infprob3 = clf3.predict_proba([DI4_DG_LIST])[0][1] 
        infprob4=clf4.predict_proba([DI5_DG_LIST])[0][1]
        infprob5 = clf5.predict_proba([DM2_DG_LIST])[0][1]
        infprob6 = clf6.predict_proba([DM3_DG_LIST])[0][1] 
        infprob7 = clf7.predict_proba([DM4_DG_LIST])[0][1]
        infprob8 = clf8.predict_proba([DJ2_DG_LIST])[0][1]
        infprob9 = clf9.predict_proba([DJ4_DG_LIST])[0][1] 
        infprob10 = clf10.predict_proba([DJ6_DG_LIST])[0][1]
        infprob11 = clf11.predict_proba([DJ8_DG_LIST])[0][1]
        infprob12 = clf12.predict_proba([DI6_DG_LIST])[0][1] 
        infprob13 = clf13.predict_proba([DF2_DG_LIST])[0][1]
        infprob14 = clf14.predict_proba([DL1_DG_LIST])[0][1]
        infprob15 = clf15.predict_proba([DE1_DG_LIST])[0][1] 
        infprob16 = clf16.predict_proba([DE2_DG_LIST])[0][1]
        infprob17 = clf17.predict_proba([DH4_DG_LIST])[0][1]
        infprob18 = clf18.predict_proba([DC1_DG_LIST])[0][1] 
        infprob19 = clf19.predict_proba([DC3_DG_LIST])[0][1]
        infprob20 = clf20.predict_proba([DK8_DG_LIST])[0][1]
               
        return render_template('result.html',inf1=(infprob1*100), inf2 = (round(infprob2*100,2)), inf3 = (round(infprob3*100,2)),
                               inf4 = (round(infprob4*100,2)),
inf5 = (round(infprob5*100,2)),
inf6 = (round(infprob6*100,2)),
inf7 = (round(infprob7*100,2)),
inf8 = (round(infprob8*100,2)),
inf9 = (round(infprob9*100,2)),
inf10 = (round(infprob10*100,2)),
inf11 = (round(infprob11*100,2)),
inf12 = (round(infprob12*100,2)),
inf13 = (round(infprob13*100,2)),
inf14 = (round(infprob14*100,2)),
inf15 = (round(infprob15*100,2)),
inf16 = (round(infprob16*100,2)),
inf17 = (round(infprob17*100,2)),
inf18 = (round(infprob18*100,2)),
inf19 = (round(infprob19*100,2)),
inf20 = (round(infprob20*100,2))
)
   
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
        data = results.pandas().xyxy[0].to_json(orient="records")

        # for debugging
        # data = results.pandas().xyxy[0].to_json(orient="records")
        # return data

        results.render()  # updates results.imgs with boxes and labels
        for img in results.imgs:
            img_base64 = Image.fromarray(img)
            img_base64.save("static/image0.jpg", format="JPEG")
        with open('static/sample.json', 'w') as outfile:
            json.dump(data, outfile)

        return redirect("static/image0.jpg")

    return render_template("detect.html")
    
if __name__ == '__main__'  :
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    args = parser.parse_args()
#    model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True, force_reload=True, autoshape=True)  # force_reload = recache latest code
    model = torch.hub.load(r'C:/final_repository/flask/Main/yolov5', 'custom', path=r'C:/final_repository/flask/Main/yolov5s.pt', source='local')

#    model = torch.hub.load(r'yolov5', 'yolov5s', path=r'yolov5s.pt', source='local')

    model.eval()
    db.create_all()
    app.secret_key = "123"
    # secret_key는 서버상에 동작하는 어플리케이션 구분하기 위해 사용하고 복잡하게 만들어야 합니다.
    
    app.run(debug=True) 