# HTTP定义了与服务器交互的不同方法

from flask import Flask, request

app = Flask(__name__)

# 默认只接受GET请求
@app.route('/page')
def page():
    return 'GET请求页面'

# 接受GET和POST请求
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # 处理表单提交
        return '收到POST请求'
    else:
        # 显示表单
        return '''
        <from method="post">
            <iuput type="text" name="data">
            <button type="submit">提交</button>
        </form>
        '''


if __name__ == '__main__':
    app.run(debug=True)