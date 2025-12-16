# 1. 导入语句
from flask import Flask  # 从flask包中导入Flask类

# 2. 应用实例化
app = Flask(__name__)  # __name__ 是当前模块名称
                       # Flask使用这个参数确定应用的目录

# 3. 路由装饰器
@app.route('/')  # @app.route() 是一个装饰器，将URL路径('/')映射到下面的函数
                 # '/'表示网站跟目录(首页)

# 4. 视图函数
def hello_world():
    return 'Hello World!'
# 视图函数处理该请求，并返回响应
# 返回值可以是字符串、HTML、JSON等


# 5. 启动应用
if __name__ == '__main__':
    app.run(debug=True)
# 当直接运行此文件时，启动开发服务器
# 当debug=True 开启调试模式