from .settings import *
class User:
    def __init__(self,id, 
                first_name=None, 
                last_name=None,
                username=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.is_admin = False
        self.orders = [] # list with many order objects
    def start(self, message):
        if not self.is_admin: 
            bot.send_message(message.chat.id,f'''{self.first_name}, 
            Вітаємо Вас в магазині одягу:SuperShop!
            Оберіть,будь ласка, подальшу дію:
            ''', reply_markup=kb_user1)
        else:
            bot.send_message(message.chat.id,f'''Здравствуйте {self.first_name}, 
            с магазином в ваше отсутствие все было хорошо
            
            ''', reply_markup=kb_user1)

class Admin:
    def __init__(self,id, user):
        self.id = id
        user.is_admin = True
        self.user = user
    
class ProductType:
    def __init__(self, id, name, description):
        self.id = id 
        self.name = name 
        self.description = description 
    
class Product:
    def __init__(self, id, 
                name, 
                description, 
                price,
                photo, 
                product_type):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.photo = photo
        self.producttype = product_type
class Order:
    def __init__(self, id):
        self.id = id
        self.products = [] # list with many product objects 
    def add_product(self, product):
        pass
    def remove_product(self, product):
        pass

users_list = []
admin_list = []
product_types_list = []
orders_list = []
product_list = []