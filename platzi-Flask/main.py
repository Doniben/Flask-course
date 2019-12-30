from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    
    response = make_response(redirect('/hello'))
    response.set_cookie('usr_ip', user_ip)

    return response

@app.route('/hello')
def hello():
    usern_ip = request.cookies.get('user_ip')
    return render_template('hello.html', userfront_ip=usern_ip)

