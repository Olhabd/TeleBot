from modules.settings import *
from modules.user import *
from modules.admin import *

class User:
    def __init__(self,id, 
                first_name=None, 
                last_name=None,
                username=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.is_admin = admins
        self.orders = [] # list with many order objects
    def start(self, message):
        if not self.is_admin:
            bot.send_message(message.chat.id,f'''{self.first_name}, 
            Вітаємо Вас в магазині одягу:SuperShop!
            Оберіть,будь ласка, подальшу дію:
            ''', reply_markup=kb_user1)
        else:
            bot.send_message(message.chat.id,f'''Вітаємо {self.first_name}, 
            у магазині все було гаразд, за час вашої відсутності.
            
            ''', reply_markup= kb_admins_start)

class Admin:
    def __init__(self,id, user):
        self.id = id
        user.is_admin = True
        self.user = user
    
class ProductType:
    def __init__(self, id, name):
        self.id = id 
        self.name = name 

    
class Product:
    def __init__(self, id, 
                name, 
                price,
                product_type,
                photo = None, 
                ):
        self.id = id
        self.name = name
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

orders_list = []
product_list = []