# 第2天： Flask路由与视图函数 + 前端基础入门


# 路由器的转换类型
转换器             说明                          示例
-------------------------------------------------------------
string            默认,接受不含斜杠的文本          <username>
int               接受正整数                     <int:post_id>
float             接受浮点数                     <float:price>   
path              类似string,但可以含斜杠         <path:subpath>
uuid              接受UUID字符串                 <uuid:id>


# 自定义转换类型
from werkzeug.routing import BaseConverter

class PhoneNumberConverter(BaseConverter):
    regex = r'\d{3}-\d{4}-\d{4}'  # 123-4567-8901格式

app.url_map.converters['phone'] = PhoneNumberConverter

@app.route('/call/<phone:number>')
def call(number):
    return f'正在呼叫: {number}'


# # HTTP定义了与服务器交互的不同方法
from flask import Flask, request

app = Flask(__name__)

#默认只接受GET请求
@app.route('/page')
def page():
    return 'GET请求页面'

#接受GET和POST请求
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        #处理表单提交
        return '收到POST请求'
    else:
        #显示表单
        return '''
        <from method="post">
            <iuput type="text" name="data">
            <button type="submit">提交</button>
        </form>
        '''


# GET 和 POST 的区别
1.数据传输方式
GET请求：参数直接拼接在URL中（如 ?name=Tom），通过地址栏可见
POST请求‌：参数放在HTTP请求的正文（Body）中，不会暴露在URL上

2.安全性与可见性
GET参数完全公开‌：URL中的参数会被浏览器记录、缓存，甚至保存在历史记录中，不适合传输密码等敏感信息
POST相对更安全‌：参数不显示在URL中，仅通过请求体传输，但HTTPS加密才是真正的安全保障

3.数据长度限制
GET有严格长度限制‌：因参数在URL中，浏览器和服务器通常限制在 2KB–8KB（如IE限制 2083 字符）
POST无明确限制‌：数据通过请求体发送，可传输大量内容（如文件上传）


# 前端基础: HTML表单
HTML 基本结构
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>我的页面</title>
</head>
<body>
    <!-- 页面内容 -->
</body>
</html>

常用表单元素
<form method="post" action="/submit">

    <!-- 文本框 -->
    <label for="name">姓名：</label>
    <input type="text" id="name" name="username" placeholder="请输入姓名">
    
    <!-- 密码框 -->
    <label for="pwd">密码：</label>
    <input type="password" id="pwd" name="password">
    
    <!-- 单选按钮 -->
    <label>
        <input type="radio" name="gender" value="male"> 男
    </label>
    <label>
        <input type="radio" name="gender" value="female"> 女
    </label>
    
    <!-- 复选框 -->
    <label>
        <input type="checkbox" name="hobby" value="reading"> 阅读
    </label>
    
    <!-- 下拉选择 -->
    <select name="city">
        <option value="beijing">北京</option>
        <option value="shanghai">上海</option>
    </select>
    
    <!-- 文本域 -->
    <textarea name="message" rows="4" cols="50"></textarea>
    
    <!-- 提交按钮 -->
    <button type="submit">提交</button>
    <!-- 或 -->
    <input type="submit" value="提交">
</form>


# 前端美化 - CSS基础
1.三种添加CSS的方式：
<!-- 1. 行内样式（不推荐大量使用） -->
<div style="color: red; font-size: 20px;">红色文字</div>
<!-- 2. 内部样式表 -->
<head>
    <style>
        .my-class {
            color: blue;
            font-size: 16px;
        }
    </style>
</head>
<!-- 3. 外部样式表（推荐） -->
<link rel="stylesheet" href="styles.css">

2.常用CSS属性和选择器
/* 基本选择器 */

/* 元素选择器 */
p {
    color: #333;
    font-size: 14px;
}

/* 类选择器 */
.my-class {
    background-color: #f0f0f0;
    padding: 10px;
}

/* ID选择器 */
#main-content {
    width: 800px;
    margin: 0 auto;
}

/* 常用属性 */
.container {
    /* 盒模型 */
    width: 100%;          /* 宽度 */
    max-width: 1200px;    /* 最大宽度 */
    margin: 0 auto;      /* 上下0，左右自动（居中） */
    padding: 20px;       /* 内边距 */
    border: 1px solid #ddd; /* 边框 */
    
    /* 背景 */
    background-color: #fff;
    background-image: url('bg.jpg');
    
    /* 字体 */
    font-family: Arial, sans-serif;
    font-size: 16px;
    line-height: 1.5;
    color: #333;
    
    /* 布局 */
    display: block;       /* 块级元素 */
    display: flex;        /* 弹性盒 */
    position: relative;   /* 定位 */
    
    /* 其他 */
    border-radius: 5px;   /* 圆角 */
    box-shadow: 0 2px 5px rgba(0,0,0,0.1); /* 阴影 */
}


# 联系人管理系统
CMS  项目结构
contact_manager/
├── app.py
├── contacts.py    # 数据管理模块
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── templates/
    ├── base.html
    ├── index.html
    └── add_contact.html

需要新增搜索功能及页面  ✔
删除按钮是删除所有联系人  ✔
为联系人添加编辑功能  ✔


# 扩展任务
为联系人添加头像上传功能
添加分页显示功能（每页显示5个联系人）
使用JavaScript添加表单验证
添加响应式设计，适配手机屏幕
