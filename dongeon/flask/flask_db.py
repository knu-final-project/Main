from flask import Flask
from flask.templating import render_template
from db129.db129 import Food

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '''
    <h1>이건 h1 제목</h1>
    <p>이건 p 본문 </p>
    <a href="https://flask.palletsprojects.com">Flask 홈페이지 바로가기</a>
    '''

@app.route('/db')
def db():
    food_list = Food().get_table();
    return render_template("test1.html", food_list = food_list)

# @app.route('/user/<user_name>/<int:user_id>') # route() 데코레이터. @는 파이썬 데코레이터.
# def user(user_name, user_id):
    
#     user_id2 = str(int(user_id) * 3)
    
#     return f'Hello, {user_name}({user_id2})!'

if __name__ == '__main__':
    app.run(debug=True) # debug True 면 코드 수정할 때 마다 Flask가 인식하고 다시 시작함.