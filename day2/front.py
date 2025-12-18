from flask import Flask, request

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 获取表单数据
        username = request.form.get('username')
        password = request.form.get('password')
        gender = request.form.get('gender')

        # 处理复选框
        hobbies = request.form.getlist('hobby')

        return f'''
        注册成功！ <br>
        用户名: {username}<br>
        性别: {password}<br>
        爱好: {" ,".join(hobbies)}
        '''

    # GET请求: 显示表单
    return '''
    <!doctype html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>用户注册</title>
    </head>
    
    <body>
        <h2>用户注册</h2>
        <form method="POST">
            <div>
                <label>用户名: </label>
                <input type="text" name="username" required>
            </div>
            <div>
                <label >密码: </label>
                <input type="text" name="password" required>
            </div>
            <div>
                <label>性别: </label>
                <input type="radio" name="gender" value="male" checked>男
                <input type="radio" name="gender" value="female">女
            </div>
            <div>
                <label>爱好: </label>
                <input type="checkbox" name="hobby" value="reading">阅读
                <input type="checkbox" name="hobby" value="sports">运动
                <input type="checkbox" name="hobby" value="music">音乐
            </div>
            <div>
                <label>城市: </label>
                <select name="city">
                    <option value="beijing">北京</option>
                    <option value="shanghai">上海</option>
                </select>
            </div>
            <div>
                <button type="submit">注册</button>
            </div>
        </form>
    </body>
    </html>
    '''


@app.route('/styled-form', methods=['GET', 'POST'])
def styled_form():
    if request.method == 'POST':
        # 处理表单数据...
        pass

    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>美化表单</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Arial', sans-serif;
                background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }

            .form-container {
                background: white;
                border-radius: 10px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
                width: 100%;
                max-width: 400px;
                padding: 30px;
            }

            h2 {
                text-align: center;
                color: #333;
                margin-bottom: 30px;
                font-size: 28px;
            }

            .form-group {
                margin-bottom: 20px;
            }

            label {
                display: block;
                margin-bottom: 5px;
                color: #555;
                font-weight: 500;
            }

            input[type="text"],
            input[type="password"],
            input[type="email"] {
                width: 100%;
                padding: 12px 15px;
                border: 2px solid #ddd;
                border-radius: 5px;
                font-size: 16px;
                transition: border-color 0.3s;
            }

            input:focus {
                outline: none;
                border-color: #4a90e2;
            }

            button {
                width: 100%;
                padding: 12px;
                background: linear-gradient(135deg, #4a90e2 0%, #357ae8 100%);
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 18px;
                font-weight: 600;
                cursor: pointer;
                transition: transform 0.2s, box-shadow 0.2s;
            }

            button:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(74, 144, 226, 0.4);
            }

            .form-footer {
                text-align: center;
                margin-top: 20px;
                color: #666;
            }

            .form-footer a {
                color: #4a90e2;
                text-decoration: none;
            }

            .form-footer a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="form-container">
            <h2>用户注册</h2>
            <form method="post">
                <div class="form-group">
                    <label for="username">用户名</label>
                    <input type="text" id="username" name="username" 
                           placeholder="请输入用户名" required>
                </div>

                <div class="form-group">
                    <label for="email">邮箱</label>
                    <input type="email" id="email" name="email" 
                           placeholder="example@email.com" required>
                </div>

                <div class="form-group">
                    <label for="password">密码</label>
                    <input type="password" id="password" name="password" 
                           placeholder="至少6位字符" required>
                </div>

                <button type="submit">注册账号</button>

                <div class="form-footer">
                    <p>已有账号？<a href="#">立即登录</a></p>
                </div>
            </form>
        </div>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run()