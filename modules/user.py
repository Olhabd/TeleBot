from modules.models import *
from modules.settings import *
from modules.admin import *

def find_user(id):
    user = False
    for user_temp in users_list:
        if user_temp.id == id:
            user = user_temp
            break
    if not user:
        return False
    return user


def view_product_types():

    # Вывод всех категррий продуктов как кнопок
    # keyboard = types.Keyboard
    # for category in categories:
        # btn = types.Button(category.name, callback_data = category.id)
        # keyboard.add(btn)
    



def view_products(cd):
    for category in categories:
        if category.id == cd:
            current_category = category
            break
    for product in product_list:
        if product.producttype == current_category:
            # bot.sendmessage Name: name 