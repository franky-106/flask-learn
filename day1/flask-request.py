from flask import Flask, request
from flask import make_response

app = Flask(__name__)

@app.route('/greeting', methods=['GET', 'POST'])
def greet():
    method = request.method

    if method == 'GET':
        return '''
        <form method="POST">
            <label>你的名字：</label>
            <input type="text" name="username">
            <button type="submit">提交</button>
        </form>
        '''
    elif method == 'POST':
        # POST请求：处理表单数据
        username = request.form.get('username', '陌生人')
        return f'<h1>你好，{username}！</h1>'

@app.route('/custom-response')
def custom_response():
    # 创建自定义响应
    response = make_response('<h1>BOOM!</h1>')
    response.status_code = 201
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response


if __name__ == '__main__':
    app.run(debug=True)