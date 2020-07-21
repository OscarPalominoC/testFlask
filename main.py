from flask import Flask, request, make_response, redirect, render_template, session
from app import create_app

app = create_app()

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response


@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')

    return render_template('hello.html')
