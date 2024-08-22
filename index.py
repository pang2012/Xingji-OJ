from flask import Flask, render_template, redirect,request,session,make_response
import threading,time,easygui
import subprocess,hashlib,os,random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
#POP3/SMTP:DMXIGRXAKFDBLYAQ
#
app = Flask(__name__)

nowques=None
app.secret_key = 'c4d038b4bed09fdb1471ef51ec3a32cd'

online=[]
onlineip=[]

yzcode={}
 
@app.route('/')
def index():
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    user_ip = request.remote_addr
    if (user_ip in onlineip):
        return render_template('login_main.html',username=online[onlineip.index(user_ip)])
    return render_template('main.html',username="")
 
 
@app.route('/login_page')
def login_page():
    return render_template('login.html')

@app.route('/sign_page')
def sign_page():
    return render_template('sign.html')

@app.route('/main_page')
def main_page():
    return render_template('main.html',username="")

@app.route('/sendyzcode')
def send_yzcode():
    # 邮件发送者和接收者
    sender = 'm15921912598@163.com'
    receiver = request.values.get("phone")
    # 邮件主题和内容
    subject = '欢迎使用XingJi Soft OJ!'
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    user_ip = request.remote_addr
    yzcode[user_ip]=str(random.randint(10000000,99999999))
    content = '您的验证码:'+yzcode[user_ip]+"验证码在注册前有效,为了保证注册安全,请勿将该验证码泄露给他人。"
     
    # 创建邮件对象
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(sender, 'utf-8')
    message['To'] = Header(receiver, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
     
    # 登录网易邮箱SMTP服务器的相关信息
    smtp_server = 'smtp.163.com'
    username = 'm15921912598@163.com'
    password = 'DMXIGRXAKFDBLYAQ'  # 注意这里不是网易邮箱的密码，而是生成的授权码
     
    # 发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server, 25)  # 连接SMTP服务器
        smtp.login(username, password)  # 登录邮箱
        smtp.sendmail(sender, receiver, message.as_string())  # 发送邮件
        print('邮件发送成功')
    except Exception as e:
        print('邮件发送失败: ', e)
    finally:
        smtp.quit()  # 断开连接
    response = make_response('')
    response.status_code = 204  # 设置状态码为204无内容
    return response

@app.route('/login_main_page <username>')
def login_main_page(username):
    #username = session.get('username')
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    user_ip = request.remote_addr
    usern=online[onlineip.index(user_ip)]
    if (usern!=username):
        return "你个酸萝卜别吃，我好不容易做的网页，你却给我投机取巧，是当我们是伞兵吗？我警告你，你再这样做，下场不会好。我劝你耗子尾汁，改过自新。"
    if not(username in online):
        return "你个酸萝卜别吃，我好不容易做的网页，你却给我投机取巧，是当我们是伞兵吗？我警告你，你再这样做，下场不会好。我劝你耗子尾汁，改过自新。"
    return render_template('login_main.html',username=username)

@app.route('/rank_page <username>')
def rank_page(username):
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    user_ip = request.remote_addr
    usern=online[onlineip.index(user_ip)]
    if (usern!=username):
        return "你个酸萝卜别吃，我好不容易做的网页，你却给我投机取巧，是当我们是伞兵吗？我警告你，你再这样做，下场不会好。我劝你耗子尾汁，改过自新。"
    if not(username in online):
        return "你个酸萝卜别吃，我好不容易做的网页，你却给我投机取巧，是当我们是伞兵吗？我警告你，你再这样做，下场不会好。我劝你耗子尾汁，改过自新。"
    return render_template('rank.html',username=username)

@app.route('/problems <username>')
def problems_page(username):
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    user_ip = request.remote_addr
    usern=online[onlineip.index(user_ip)]
    try:
        #return render_template('problem.html',username=username)
        if (usern!=username):
            return "你个酸萝卜别吃，我好不容易做的网页，你却给我投机取巧，是当我们是伞兵吗？我警告你，你再这样做，下场不会好。我劝你耗子尾汁，改过自新。"
        if not(username in online):
            return "你个酸萝卜别吃，我好不容易做的网页，你却给我投机取巧，是当我们是伞兵吗？我警告你，你再这样做，下场不会好。我劝你耗子尾汁，改过自新。"
        return render_template('problem.html',username=username)
    except:
        return render_template('login.html',loginmsg="请先登录再使用题库")

@app.route('/login')
def login():
    global online
    username = request.values.get("username")
    password = request.values.get("password")
    alluserf=open("static/userdata/username.txt","r")
    allpasswordf=open("static/userdata/userpassword.txt","r")
    alluser=alluserf.readlines()
    allpassword=allpasswordf.readlines()
    alluserf.close()
    allpasswordf.close()
    password=hashlib.md5(password.encode("utf-8")).hexdigest()
    if (username in online):
        return render_template('login.html',loginmsg="此账号已在其他设备登录")
    for i in range(len(alluser)):
        if (alluser[i].strip("\n")==username and password==allpassword[i].strip("\n")):
            #session['username'] = username
            x_forwarded_for = request.headers.get('X-Forwarded-For')
            user_ip = request.remote_addr
            online.append(username)
            onlineip.append(user_ip)
            return render_template('login_main.html',username=username)
    return render_template('login.html',loginmsg="账号或密码错误")

@app.route('/signin')
def signin():
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    user_ip = request.remote_addr
    username = request.values.get("username")
    password = request.values.get("password")
    yzm = request.values.get("yzcode")
    try:
        if (yzm!=yzcode[user_ip]):
            return "验证码错误"
    except:
        pass
        #return "请先发送验证码"
    for i in username:
        if (i==' '):
            return "用户名不能包含空格"
        if not(i.isalpha()) and not(i.isalnum()):
            return "密码只能包含英文字符"
    if username=="":
        return "用户名不能为空"
    if password=="":
        return "密码不能为空"
    for i in password:
        if (i==' '):
            return "密码不能包含空格"
        if not(i.isalpha()) and not(i.isalnum()):
            return "密码只能包含英文字符"
    allusernames=open("static/userdata/username.txt","r")
    alluserpasswords=open("static/userdata/userpassword.txt","r")
    usernames=allusernames.read()
    usernames=usernames.split("\n")
    if (username in usernames):
        return "用户名已存在"
    allusernames.close()
    alluserpasswords.close()
    allusernames=open("static/userdata/username.txt","a")
    alluserpasswords=open("static/userdata/userpassword.txt","a")
    password=hashlib.md5(password.encode("utf-8")).hexdigest()
    allusernames.write("\n"+username)
    alluserpasswords.write("\n"+password)
    allusernames.close()
    alluserpasswords.close()
    online.append(username)
    onlineip.append(user_ip)
    return render_template('login_main.html',username=username)
@app.route('/problem <name>-<username>')
def problemsxx_page(name,username):
    #try:
        #global nowques
        #nowques=name
    return render_template('questions/'+name+'.html',username=username)
    #except:
        #return render_template('login.html',loginmsg="请先登录再使用题库")

@app.route('/submit<name> <language> <ques>', methods=['POST'])
def submit(name,language,ques):
    text = request.form['code']
    # 处理text...
    print('Text received: {}'.format(text))
    output=None
    def judge(name):
        global output
        f=open("submit/"+name,"w")
        f.write(text)
        f.close()
        # 使用subprocess.run来运行外部程序
        process = subprocess.run(['python',"judger.py", name,'submit/'+name,language], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #process.wait()
        output = process.stdout
        

    thread = threading.Thread(target=lambda:judge(name))
    thread.start()
    f=open("data.log","r")
    output=f.read()
    f.close()
    response = make_response('')
    response.status_code = 204  # 设置状态码为204无内容
    return response

@app.route('/getsubmit')
def getsubmit():
    f=open("data.log","r")
    output=f.read()
    f.close()
    output=output.split('\n')
    
    return {"提交结果":output[-2],"您的代码正确率":output[-1]+"%"}

@app.route('/images/<path:path>')
def send_image(path):
    # 假设图片存储在static/images目录下
    return app.send_static_file("images/"+path)

@app.route('/css/<path:path>')
def send_css(path):
    # 假设css存储在static/css目录下
    return app.send_static_file("css/"+path)

@app.route('/js/<path:path>')
def send_js(path):
    #存储在static/js目录下
    return app.send_static_file("js/"+path)

@app.route('/close_page <username>')
def close_page(username):
    global online,onlineip
    for i in range(len(online)):
        if (online[i]==username):
            online.pop(i)
            onlineip.pop(i)
    return render_template('main.html',username="")
 
if __name__ == '__main__':
    app.config['SERVER_NAME'] = '192.168.124.7:5000'
    app.run(debug=True)