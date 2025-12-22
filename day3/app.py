from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime


app = Flask(__name__)
bootstrap = Bootstrap(app)


# 后端传递数据到模板
@app.route('/user/<username>')
def show_user(username):
    return render_template('user.html',
                          username=username,
                          is_admin=True,
                          items=['苹果', '香蕉', '橙子'])

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%Y-%m-%d %H:%M:%S'):
    """自定义日期格式化过滤器"""
    if value is None:
        return ""
    return value.strftime(format)

@app.template_filter('phone_format')
def phone_format(value):
    """电话号码格式化"""
    if not value:
        return ""
    return f"{value[:3]}-{value[3:7]}-{value[7:]} "


if __name__ == '__main__':
    app.run(debug=True)