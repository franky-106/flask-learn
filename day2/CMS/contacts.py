class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, email, phone):
        """添加联系人"""
        contact = {
            'id': len(self.contacts) + 1,
            'name': name,
            'email': email,
            'phone': phone,
        }
        self.contacts.append(contact)
        return contact

    def get_all_contacts(self):
        """获取所有联系人"""
        return self.contacts

    def search_contact(self, keyword):
        """搜索联系人"""
        keyword = keyword.lower()
        return [
            contact for contact in self.contacts
            if (keyword in contact['name'].lower() or
                keyword in contact['email'].lower() or
                keyword in contact['phone'])
        ]

    def delete_contact(self, contact_id):
        """删除联系人"""
        self.contacts = [c for c in self.contacts if c['id'] != contact_id]
        return True

    def edit_contact(self, id, name, email, phone):
        """更改联系人信息"""
        index = id - 1

        if index < 0 or index >= len(self.contacts):
            return False

        # 修改对应位置的联系人信息
        self.contacts[index] = {
            'id': id,
            'name': name,
            'email': email,
            'phone': phone,
        }
        return True

    '''
    # contacts.py 添加新方法
    def get_contact_by_id(self, contact_id):
        """根据ID获取联系人"""
        for contact in self.contacts:
            if contact['id'] == contact_id:
                return contact
        return None
    
    
    # 当前方法在删除联系人后可能出错
    # 建议改进：通过ID查找而不是索引
    def edit_contact(self, contact_id, name, email, phone):
        for contact in self.contacts:
            if contact['id'] == contact_id:
                contact['name'] = name
                contact['email'] = email
                contact['phone'] = phone
                return True
        return False
    '''