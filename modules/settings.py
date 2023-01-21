import telebot
from modules.user import *
from modules.models import *
from modules.admin import *
# from modules.models import list_category

bot = telebot.TeleBot('5660746331:AAEJW3cicwf76f0YVnnP_JyDy4Yzjlz4Vgo')

admins = [620080523]

kb_admins_start = telebot.types.ReplyKeyboardMarkup(True)
btn_add_category = telebot.types.InlineKeyboardButton('Додати категорію', callback_data = 'add_category')
btn_add_good = telebot.types.InlineKeyboardButton('Додати товар', callback_data = 'Додати товар')
btn_edit_good = telebot.types.InlineKeyboardButton('Редагувати товар', callback_data= 'Редагувати товар')
btn_del_good = telebot.types.InlineKeyboardButton('Видалити товар', callback_data= 'Видалити товар')
btn_orders = telebot.types.InlineKeyboardButton('Замовлення', callback_data= 'Замовлення')
btn_support = telebot.types.InlineKeyboardButton('Заявки', callback_data= 'Заявки')
kb_admins_start.add(btn_add_category, btn_add_good, btn_edit_good, btn_del_good, btn_orders, btn_support)

kb_add_category = telebot.types.ReplyKeyboardMarkup(True)
btn_back = telebot.types.InlineKeyboardButton('Назад', callback_data= 'Назад')
kb_add_category.add(btn_back)

list_category = []

kb_add_good = telebot.types.ReplyKeyboardMarkup(True)
btn_back_good = telebot.types.InlineKeyboardButton('Назад', callback_data= 'Назад')
kb_add_good.add(btn_back_good)
for category in list_category:
    category = telebot.types.InlineKeyboardButton(text=category,
                                            callback_data=category)
    kb_add_good.add(category)

kb_edit_good = telebot.types.ReplyKeyboardMarkup(True)
btn_back_edit = telebot.types.InlineKeyboardButton('Назад', callback_data= 'Назад')
kb_edit_good.add(btn_back_edit)
for category in list_category:
    category = telebot.types.InlineKeyboardButton(text=category,
                                            callback_data=category)
    kb_edit_good.add(category)

kb_del_good = telebot.types.ReplyKeyboardMarkup(True)
btn_back_del = telebot.types.InlineKeyboardButton('Назад', callback_data= 'Назад')
kb_edit_good.add(btn_back_del)
for category in list_category:
    category = telebot.types.InlineKeyboardButton(text=category,
                                            callback_data='')
    kb_del_good.add(category)

users_list = []

kb_user_orders = telebot.types.ReplyKeyboardMarkup(True)
btn_back_usorders = telebot.types.InlineKeyboardButton('', callback_data= '')
kb_user_orders.add(btn_back_usorders)
for user in users_list:
    user = telebot.types.InlineKeyboardButton(text=user,
                                            callback_data='')
    kb_user_orders.add(user)

requestes = []

kb_admin_support = telebot.types.ReplyKeyboardMarkup(True)
btn_back_support =  telebot.types.InlineKeyboardButton('', callback_data= '')
kb_admin_support.add(btn_back_support)
for request in requestes:
    request = telebot.types.InlineKeyboardButton(text=request,
                                            callback_data='')
    kb_user_orders.add(request)

kb_user1 = telebot.types.ReplyKeyboardMarkup(True)
btn_category = telebot.types.InlineKeyboardButton('Категорії',callback_data= 'Категорії')
btn_wishlist = telebot.types.InlineKeyboardButton('Список бажань',callback_data= 'Список бажань')
btn_orders = telebot.types.InlineKeyboardButton('Мої замовлення', callback_data='Мої замовлення')
btn_support_us = telebot.types.InlineKeyboardButton('Підтримка', callback_data='Підтримка')
kb_user1.add(btn_category,btn_wishlist, btn_orders, btn_support_us)

kb_category = telebot.types.ReplyKeyboardMarkup(True)
btn_back_us1 = telebot.types.InlineKeyboardButton('', callback_data= '')
kb_category.add(btn_back_us1)
for category in list_category:
    category = telebot.types.InlineKeyboardButton(text=category,
                                            callback_data='')
    kb_category.add(category)

wishlist = []

kb_wishlist = telebot.types.ReplyKeyboardMarkup(True)
btn_back_category = telebot.types.InlineKeyboardButton('', callback_data= '')
for wish in wishlist:
    wish = telebot.types.InlineKeyboardButton(text=wish,
                                            callback_data='')
    kb_wishlist.add(wish)

orders_list = []

kb_orders = telebot.types.ReplyKeyboardMarkup(True)
btn_back_wl = telebot.types.InlineKeyboardButton('', callback_data= '')
for order in orders_list:
    wish = telebot.types.InlineKeyboardButton(text=order,
                                            callback_data='')
    kb_orders.add(order)

kb_support = telebot.types.ReplyKeyboardMarkup(True)
btn_request =  telebot.types.InlineKeyboardButton('', callback_data= '')
btn_back_orders = telebot.types.InlineKeyboardButton('', callback_data= '')
kb_support.add(btn_request,btn_back_orders)