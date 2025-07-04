from flask import Flask, render_template, request, redirect, make_response, session
import sqlite3
import re  # for email validation
from crawler import crawl_news


app = Flask(__name__)
app.secret_key = 'Gail secret key'

#  檢查 Email 格式的函式
def is_valid_email(email):
   return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# 🔸 首頁
@app.route('/home')
def home():
    if "logined" in session and session["logined"] == "1":
        name = request.cookies.get('userName')
        return render_template('home.html', userName=name)
    else:
        return redirect('/login')
    
@app.route("/css")
def css():
    return render_template(r"home.html") 

#  登入頁（GET）
@app.route('/login', methods=['GET'])
def login_form():
    name = request.cookies.get('userName')
    return render_template('login.html', userName=name)

@app.route("/news", methods=["GET", "POST"]) # 新聞
def news():
    news_list = crawl_news()
    return render_template("news.html", news_list=news_list)

#  登入處理（POST）
@app.route('/login', methods=['POST'])
def login():
    user = request.form['user']
    passwd = request.form['passwd']
    name = request.form['name']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (user,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        db_passwd = result[2]
        db_name = result[3]
        if passwd == db_passwd:
            resp = make_response(render_template('home.html', userName=db_name))
            resp.set_cookie('userName', db_name)
            session['logined'] = "1"
            return resp
        else:
            return "登入失敗，密碼不正確"
    else:
        return "登入失敗，帳號不正確"

#  註冊頁（GET）
@app.route('/register', methods=['GET'])
def register_form():
    return render_template('register.html')

# 註冊處理（POST）
@app.route('/register', methods=['POST'])
def register():
    user = request.form['user']
    passwd = request.form['passwd']
    name = request.form['name']
    email = request.form['email']

    # 驗證 Email 格式
    if not is_valid_email(email):
        return "註冊失敗：Email 格式錯誤"

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password, name, email) VALUES (?, ?, ?, ?)",
                       (user, passwd, name, email))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return "註冊失敗：帳號或 Email 已存在"
    
    conn.close()
    return redirect('/login')



#  登出
@app.route('/logout')
def logout():
    session.pop('logined', None)
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
