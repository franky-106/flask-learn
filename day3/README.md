# Jinja2 基本语法回顾
Jinja2是Flask默认的模板引擎

后端传递数据到模板
@app.route('/user/<username>')
def show_user(username):
    return render_template('user.html', 
                          username=username,
                          is_admin=True,
                          items=['苹果', '香蕉', '橙子'])


<!-- templates/user.html -->
<!DOCTYPE html>
<html>
<head>
    <title>用户页面</title>
</head>
<body>
    {# 这是Jinja2注释，不会出现在HTML中 #}

    <!-- 1. 变量输出 -->
    <h1>欢迎，{{ username }}!</h1>
    
    <!-- 2. 条件判断 -->
    {% if is_admin %}
        <p>您有管理员权限</p>
    {% else %}
        <p>您是普通用户</p>
    {% endif %}
    
    <!-- 3. 循环 -->
    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
    
    <!-- 4. 过滤器 -->
    <p>用户名大写: {{ username|upper }}</p>
    <p>列表长度: {{ items|length }}</p>
    <p>默认值: {{ variable_not_exist|default('默认值') }}</p>
    <p>日期格式化: {{ current_time|datetimeformat('%Y-%m-%d') }}</p>
    
    <!-- 5. 转义 -->
    <p>安全输出HTML: {{ html_content|safe }}</p>
    <p>不转义: {{ html_content }}</p>
</body>
</html>

# 常用过滤器
常用内置过滤器
{{ name|capitalize }}        # 首字母大写
{{ name|lower }}             # 转换为小写
{{ name|upper }}             # 转换为大写
{{ name|title }}             # 每个单词首字母大写
{{ name|trim }}              # 移除首尾空白
{{ value|default('默认值') }} # 设置默认值
{{ list|length }}            # 获取长度
{{ list|sort }}              # 排序
{{ list|reverse }}           # 反转
{{ string|replace('old', 'new') }} # 替换
{{ string|truncate(20) }}    # 截断字符串
{{ number|round(2) }}        # 四舍五入


# Bootstrap前端框架
Bootstrap是一个流行的前端框架，用于快速开发响应式网站
它提供了丰富的CSS和JavaScript组件，简化了网页设计和布局

Bootstrap常用组件
<!-- 按钮 -->
<button class="btn btn-primary">主要按钮</button>
<button class="btn btn-secondary">次要按钮</button>
<button class="btn btn-success">成功按钮</button>
<button class="btn btn-danger">危险按钮</button>
<button class="btn btn-warning">警告按钮</button>
<button class="btn btn-info">信息按钮</button>

<!-- 卡片 -->
<div class="card" style="width: 18rem;">
    <img src="..." class="card-img-top" alt="...">
    <div class="card-body">
        <h5 class="card-title">卡片标题</h5>
        <p class="card-text">卡片内容。</p>
        <a href="#" class="btn btn-primary">按钮</a>
    </div>
</div>

<!-- 表单 -->
<form>
    <div class="mb-3">
        <label for="email" class="form-label">邮箱地址</label>
        <input type="email" class="form-control" id="email">
        <div class="form-text">我们不会分享你的邮箱。</div>
    </div>
    <div class="mb-3">
        <label for="password" class="form-label">密码</label>
        <input type="password" class="form-control" id="password">
    </div>
    <div class="mb-3 form-check">
        <input type="checkbox" class="form-check-input" id="remember">
        <label class="form-check-label" for="remember">记住我</label>
    </div>
    <button type="submit" class="btn btn-primary">提交</button>
</form>

<!-- 警告框 -->
<div class="alert alert-success" role="alert">
    操作成功！
</div>
<div class="alert alert-danger" role="alert">
    出错了！
</div>


