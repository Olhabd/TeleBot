from modules.user import *
from modules.models import *
from modules.settings import *
import re 
def add_product(text): # get  message.text
    # Проверяем на то что он подходит под следующий патерн 
    # Название, цена, тип продукта получаем эти значения в переменную
    pass

    # Перебираем список product_types_list если тип продукта с таким именем уже есть 
    # то дейтсвий не требуется, иначе
    #  categories.append(ProductType(categories[-1].id + 1, type_product))

    # product_list.append(Product(product_list[-1].id + 1, name, price, product_type))