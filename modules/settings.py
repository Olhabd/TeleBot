import telebot
from .models import *
from .user import *

bot = telebot.TeleBot('5660746331:AAEJW3cicwf76f0YVnnP_JyDy4Yzjlz4Vgo')

admins = [620080523, 542387853]

kb_admins1 = telebot.types.ReplyKeyboardMarkup(True)
btn_goods = telebot.types.InlineKeyboardButton('Товар', callback_data= 'Товар')
btn_user_orders = telebot.types.InlineKeyboardButton('Замовлення', callback_data= 'Замовлення')
btn_support = telebot.types.InlineKeyboardButton('Підтримка', callback_data= 'Підтримка')
btn_add_admin = telebot.types.InlineKeyboardButton('Додати адміністратора', callback_data= 'Додати адміністратора')
kb_admins1.add(btn_goods,btn_user_orders,btn_support,btn_add_admin)

kb_goods = telebot.types.ReplyKeyboardMarkup(True)
btn_add = telebot.types.InlineKeyboardButton('Додати товар',callback_data= 'Додати товар')
btn_edit = telebot.types.InlineKeyboardButton('Редагувати товар', callback_data= 'Редагувати товар')
btn_del = telebot.types.InlineKeyboardButton('Видалити товар',callback_data= 'Видалити товар')
btn_back_goods = telebot.types.InlineKeyboardButton('Назад',callback_data= 'Назад')
kb_goods.add(btn_add,btn_edit,btn_del,btn_back_goods)


kb_add_good = telebot.types.ReplyKeyboardMarkup(True)

list_category = {
    "Women's Clothing" : {},
    "Accessories" :  {},
    "Shoes" : {},
    "Outerwear": {},    
}

kb_user_orders = telebot.types.ReplyKeyboardMarkup(True)
#кнопки(список) категорій товару -> кнопки замовлених товарів(список)
#інфа про замовника + замовленний товар -> кнопки(статус замовлення, особ.чат)

kb_user1 = telebot.types.ReplyKeyboardMarkup(True)
btn_category = telebot.types.InlineKeyboardButton('Категорії',callback_data= 'Категорії')
btn_wishlist = telebot.types.InlineKeyboardButton('Список бажань',callback_data= 'Список бажань')
btn_orders = telebot.types.InlineKeyboardButton('Мої замовлення', callback_data='Мої замовлення')
kb_user1.add(btn_category,btn_wishlist, btn_orders)

