from modules.user import *
from modules.admin import *
@bot.message_handler(commands=["start"]) 
def start(message):
    user = find_user(message.chat.id)
    if user:
        user.start(message)
    else:
        user = User(message.chat.id,
                    message.from_user.first_name,
                    message.from_user.last_name,
                    message.from_user.username,)
        users_list.append(user)
        user.start(message)
@bot.message_handler(commands=['add'])
def add(message):
    msg = bot.send_message(message.chat.id, 'Введіть новий товар')
    bot.register_next_step_handler(msg,get_info_about_product_for_add)
def get_info_about_product_for_add(message):
    add_product(message.text)
@bot.message_handler(commands=['products'])
def products(message):
    bot.send_message(message.chat.id, 'Оберіть категорію', reply_markup=view_product_types())
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'Додати категорію':
        bot.send_message(call.message.chat.id, 'Введіть категорію', reply_markup = kb_add_category)
    elif call.data == 'Додати товар':
        bot.send_message(call.message.chat.id, 'Оберіть категорію',reply_markup= kb_add_good )


bot.infinity_polling()   