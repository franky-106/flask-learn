from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def welcome():
    return '<h1>用户你好!</h1>'

@app.route('/time')
def time_shower():
    now = datetime.now()
    current_time = now.strftime('%d.%m.%Y %H:%M:%S')
    return f'当前时间: {current_time}'

@app.route('/square/<int:num>')
def square(num):
    return f'{num * num}'


@app.route('/calculate',methods=['GET',])
def calculate():
    method = request.method
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    operation = request.args.get('operation')

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    else:
        result = num1 / num2

    return f'运算结果为: {result}'



def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


@app.errorhandler(404)
def page_not_found(error):
    return '''
    <h1>404 - 页面未找到</h1>
    <p>抱歉，您访问的页面不存在。</p>
    <p><a href="/">返回首页</a></p>
    ''', 404


if __name__ == '__main__':
    app.run(debug=True)