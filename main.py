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
@bot.message_handler(commands='admin')
def set_admin(message):
    user = find_user(message.chat.id)
    user.is_admin = True

bot.infinity_polling()   