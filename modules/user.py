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