from modules.user import *
from modules.models import *
from modules.settings import *
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

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'add_category':
        bot.send_message(call.message.chat.id, 'Введіть категорію', reply_markup = kb_add_category)
    elif call.data == 'Додати товар':
        bot.send_message(call.message.chat.id, 'Оберіть категоріюх',reply_markup= kb_add_good )

bot.infinity_polling()   