import telebot
import os

bot = telebot.TeleBot('5660746331:AAEJW3cicwf76f0YVnnP_JyDy4Yzjlz4Vgo')

admins = 620080523

kb_admins1 = telebot.types.InlineKeyboardMarkup()
btn_goods = telebot.types.InlineKeyboardButton('Товар', callback_data= 'Товар')
btn_user_orders = telebot.types.InlineKeyboardButton('Замовлення', callback_data= 'Замовлення')
btn_support = telebot.types.InlineKeyboardButton('Підтримка', callback_data= 'Підтримка')
btn_add_admin = telebot.types.InlineKeyboardButton('Додати адміністратора', callback_data= 'Додати адміністратора')
kb_admins1.add(btn_goods,btn_user_orders,btn_support,btn_add_admin)

kb_goods = telebot.types.InlineKeyboardMarkup()
btn_add = telebot.types.InlineKeyboardButton('Додати товар',callback_data= 'Додати товар')
btn_edit = telebot.types.InlineKeyboardButton('Редагувати товар', callback_data= 'Редагувати товар')
btn_del = telebot.types.InlineKeyboardButton('Видалити товар',callback_data= 'Видалити товар')
btn_back_goods = telebot.types.InlineKeyboardButton('Назад',callback_data= 'Назад')
kb_goods.add(btn_add,btn_edit,btn_del,btn_back_goods)

kb_add_good = telebot.types.InlineKeyboardMarkup()

list_category = {
    "Women's Clothing" : {},
    "Accessories" :  {},
    "Shoes" : {},
    "Outerwear": {},    
}

# categories_admin = telebot.types.InlineKeyboardMarkup()

# for key, value in telebot.categories_admin.items():
#     categories_admin.add(telebot.types.InlineKeyboardButton)

'''
Категории:
1. Верхній одяг
    1.1 Жакети
    1.2 Жилети
    1.3 Піджаки
    1.4 Плащі
    1.5 Куртки
    1.6 Пальто
2. Жін.Одяг
    2.1 Сукні
    2.2 Туніки
    2.3 Сарафани
    2.4 Футболки
    2.5 Майки
    2.6 Топи
    2.7 Сорочки
    2.8 Блузки
    2.9 Гольфи
    2.10 Светри
    2.11 Кардигани
    2.12 Кофти
    2.13 Толстовки
    2.14 Спідниці
    2.15 Штани
    2.16 Легінси
    2.17 Джинси
    2.18 Комбінезони
    2.19 Шорти
    2.20 Купальники
10. Взуття
    10.1 Балетки
    10.2 Кросівки
    10.3 Туфлі
    10.4 Босоніжки
    10.5 Чоботи
11. Аксесуари
    11.1 Шарфи
    11.2 Головні убори
    11.3 Сумки
    11.4 Браслети
    11.5 Кільця
    11.6 Окуляри
    11.7 Сережки
    11.8 Рукавички
    11.9 Ремені
    11.10 
'''

kb_user_orders = telebot.types.InlineKeyboardMarkup()
#кнопки(список) категорій товару -> кнопки замовлених товарів(список)
#інфа про замовника + замовленний товар -> кнопки(статус замовлення, особ.чат)

kb_user1 = telebot.types.InlineKeyboardMarkup() 
btn_category = telebot.types.InlineKeyboardButton('Категорії',callback_data= 'Категорії')
btn_wishlist = telebot.types.InlineKeyboardButton('Список бажань',callback_data= 'Список бажань')
btn_orders = telebot.types.InlineKeyboardButton('Мої замовлення', callback_data='Мої замовлення')
kb_user1.add(btn_category,btn_wishlist, btn_orders)

@bot.message_handler(commands=["start"])
def start(message):
    if message.chat.id == admins:
        bot.send_message(admins, f'Новий клієнт: {message.from_user.id} {message.from_user.first_name}{message.from_user.last_name}', reply_markup=kb_admins1)
    else:
        bot.send_message(message.chat.id,'''
        Вітаємо Вас в магазині одягу:{Название}!
        Оберіть,будь ласка, подалішу дію:
        ''', reply_markup=kb_user1)
        bot.send_message(admins, f'Новий клієнт: {message.from_user.id} {message.from_user.first_name}{message.from_user.last_name}', reply_markup=kb_admins1)


bot.infinity_polling()   