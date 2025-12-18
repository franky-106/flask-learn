from flask import Flask, render_template, request, redirect, url_for
from contacts import ContactManager


app = Flask(__name__)
contact_manager = ContactManager()

contact_manager.add_contact("Tom", "138-0013-8000", "Tom@example.com")
contact_manager.add_contact("Jerry", "138-0013-8001", "Jerry@example.com")


@app.route('/')
def index():
    """首页 - 显示所有联系人"""
    contacts = contact_manager.get_all_contacts()
    # 从app的template文件夹种加载指定的模板文件
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    """添加联系人"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        if name and phone:
            contact_manager.add_contact(name, email, phone)
            return redirect(url_for('index'))

    return render_template('add_contact.html')

@app.route('/search')
def search():
    """搜索联系人"""
    keyword = request.args.get('q', '')
    results = contact_manager.search_contact(keyword)
    return render_template('search_result.html',
                           results=results,
                           keyword=keyword)

@app.route('/delete/<int:contact_id>')
def delete_contact(contact_id):
    """删除联系人"""
    contact_manager.delete_contact(contact_id)
    return redirect(url_for('index'))

@app.route('/edit/<int:contact_id>', methods=["GET", "POST"])
def edit_contact(contact_id):
    """修改联系人信息"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        if name and phone:
            contact_manager.edit_contact(contact_id, name, email, phone)
            return redirect(url_for('index'))

    '''
    # 缺少处理GET请求的数据传递
    else:
        # GET请求：需要找到联系人并传递给模板
        contact = None
        for c in contact_manager.contacts:
            if c['id'] == contact_id:
                contact = c
                break
        
        if contact:
            return render_template('edit_contact.html', contact=contact)
        else:
            return redirect(url_for('index'))
    '''


if __name__ == '__main__':
    app.run(debug=True)
