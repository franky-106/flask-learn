from flask import Flask

app = Flask(__name__)


# 基本路由
@app.route('/')
def home():
    return '首页'

# 带参数的路由
@app.route('/user/<username>')
def show_user(username):
    return f'用户: {username}'

# 带类型转换的路由
@app.route('/post/<int::post_id>')
def show_post(post_id):
    return (f'文章ID: {post_id}')

# 多类型转换
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'路径: {subpath}'

