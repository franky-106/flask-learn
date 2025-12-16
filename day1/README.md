# 文件目录
flask_learning/pythonProject
├── app.py                   # 主应用文件
├── requirements.txt         # 依赖清单
└── README.md                # 项目说明



# Flask 请求-响应 流程
用户请求 → 浏览器 → 网络 → Flask服务器
                                     ↓
路由匹配 → 执行视图函数 → 生成响应
                                     ↓
Flask服务器 → 网络 → 浏览器 → 用户看到结果



# 常用的属性和方法
from flask import request

request.method   # HTTP方法：GET，POST等
request.args     # GET参数（查询字符串）
request.form     # POST表单数据
request.headers  # 请求头
request.cookies  # Cookies
request.files    # 上传的文件



# 练习1：基础路由
创建一个Flask应用，包含以下路由：

/：显示欢迎信息
/time：显示当前时间
/square/<int:num>：显示数字的平方

提示：
from datetime import datetime

@app.route('/time')
def show_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'当前时间：{current_time}'


练习2：简单计算器
创建一个路由 /calculate，接收GET参数：

num1：第一个数字

num2：第二个数字

operation：操作（add, subtract, multiply, divide）

示例URL：http://127.0.0.1:5000/calculate?num1=10&num2=5&operation=add

练习3：错误处理
添加404错误页面：

python
@app.errorhandler(404)
def page_not_found(error):
    return '''
    <h1>404 - 页面未找到</h1>
    <p>抱歉，您访问的页面不存在。</p>
    <p><a href="/">返回首页</a></p>
    ''', 404



# 可以改进的地方
1. 计算器路由的健壮性
@app.route('/calculate',methods=['GET',])
def calculate():
    method = request.method
    # 缺少参数验证，如果用户没传参数会报错
    
    # 建议改进：
    num1_str = request.args.get('num1')
    num2_str = request.args.get('num2')
    operation = request.args.get('operation')
    
    # 验证参数是否存在
    if not all([num1_str, num2_str, operation]):
        return '缺少必要参数: num1, num2, operation', 400
    
    # 验证是否为有效数字
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        return '参数必须是数字', 400
    
    # 验证操作类型是否有效
    if operation not in ['add', 'subtract', 'multiply', 'divide']:
        return '无效的操作类型，支持: add, subtract, multiply, divide', 400
    
    # 避免除零错误
    if operation == 'divide' and num2 == 0:
        return '除数不能为零', 400

2. 定义了四个算术函数但没有在视图函数中使用它们，而是重复实现了逻辑。可以这样优化：
# 定义计算函数（可以放在文件顶部）
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("除数不能为零")
    return num1 / num2

# 在路由中使用这些函数
@app.route('/calculate', methods=['GET'])
def calculate():
    # ... 参数验证代码 ...
    
    # 使用映射减少if-elif链
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    try:
        result = operations[operation](num1, num2)
        return f'运算结果为: {result}'
    except ValueError as e:
        return str(e), 400 

3. 代码结构和格式化
# 建议：相关函数分组，添加更多注释
# ===== 工具函数 =====
def add(num1, num2):
    """加法运算"""
    return num1 + num2

def subtract(num1, num2):
    """减法运算"""
    return num1 - num2

def multiply(num1, num2):
    """乘法运算"""
    return num1 * num2

def divide(num1, num2):
    """除法运算，检查除零错误"""
    if num2 == 0:
        raise ValueError("除数不能为零")
    return num1 / num2

# ===== 路由函数 =====
@app.route('/')
def welcome():
    """首页"""
    return '<h1>用户你好!</h1>'

@app.route('/time')
def time_shower():
    """显示当前时间"""
    now = datetime.now()
    current_time = now.strftime('%d.%m.%Y %H:%M:%S')
    return f'当前时间: {current_time}'

4. 添加更多功能（可选扩展）
# 1. 添加首页导航
@app.route('/')
def welcome():
    return '''
    <h1>欢迎来到我的Flask应用!</h1>
    <ul>
        <li><a href="/time">查看当前时间</a></li>
        <li><a href="/square/5">计算5的平方</a></li>
        <li><a href="/calculate?num1=10&num2=5&operation=add">10+5计算示例</a></li>
    </ul>
    '''

# 2. 添加根路径重定向
from flask import redirect

@app.route('/home')
def home():
    return redirect('/')

# 3. 添加简单的前端样式
@app.route('/styled')
def styled_page():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; }
            h1 { color: #333; }
            .container { max-width: 600px; margin: 0 auto; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>欢迎!</h1>
            <p>这是一个带有样式的页面。</p>
        </div>
    </body>
    </html>
    '''


📊 代码质量评分
项目	        得分 (满分10)	评语
功能完整性	9	            所有要求的功能都已实现
代码规范	    8	            命名规范，结构清晰
错误处理	    7	            有404处理，但参数验证不足
代码复用	    6	            定义了函数但未充分利用
用户体验	    7	            功能完整，但界面简单
总分：7.4/10 - 非常好的开始！