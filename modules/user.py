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
    kb_category = telebot.types.ReplyKeyboardMarkup(True)
    btn_back_us1 = telebot.types.InlineKeyboardButton('Назад', callback_data= 'Назад')
    kb_category.add(btn_back_us1)
    for category in list_category:
        category = telebot.types.InlineKeyboardButton(text=category.name,
                                                callback_data=category.id)
        kb_category.add(category)

    # keyboard = types.Keyboard
    # for category in list_category:
    #     btn = types.Button(category.name, callback_data= category.id)
    # keyboard.add(btn)        

    # Вывод всех категррий продуктов как кнопок
    # keyboard = types.Keyboard
    # for category in categories:
        # btn = types.Button(category.name, callback_data = category.id)
        # keyboard.add(btn)
    



def view_products(cd):
    for category in list_category:
        if category.id == cd:
            current_category = category
            break
    for product in product_list:
        if product.producttype == current_category:
            # bot.sendmessage Name: name 