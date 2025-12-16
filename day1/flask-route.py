from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '''
    <h1>欢迎来到我的第一个Flask应用！</h1>
    <p>试试这些链接：</p>
    <ul>
        <li><a href="/about">关于页面</a></li>
        <li><a href="/user/franky">个性化问候</a></li>
    </ul>
    '''

@app.route('/about')
def about():
    return '''
    <h1>关于这个应用</h1>
    <p>这是我学习Flask的第一个项目。</p>
    <p><a href="/">返回首页</a></p>
    '''

@app.route('/user/<username>')
def show_user_profile(username):
    # 动态路由：username可以时任意值
    return f'''
    <h1>你好，{username}！</h1>
    <p>这是你的个人页面。</p>
    <p><a href="/">返回首页</a></p>
    '''

if __name__ == '__main__':
    app.run(debug=True,port=500)