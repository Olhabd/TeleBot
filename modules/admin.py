# from user import *
from models import *
from settings import *
import re


def add_product(message): # get  message.text
    pattern = (r'^([а-яА-Я]+),\s([0-9]+),\s([а-яА-Я]+)$')
    # print(re.match(pattern,str).
    name = re.match((pattern,message).group(1))
    price = re.match((pattern,message).group(2))
    product_type = re.match((pattern,message).group(3))
    # Проверяем на то что он подходит под следующий патерн 
    # Название, цена, тип продукта получаем эти значения в переменную
    
    for product_type in list_category:
        if product_type in list_category:
            pass
        else:
            list_category.append(product_type(list_category[-1].id + 1, type_product))

    
    # Перебираем список product_types_list если тип продукта с таким именем уже есть 
    # то дейтсвий не требуется, иначе
    #  list_category.append(ProductType(list_category[-1].id + 1, type_product))

    # product_list.append(Product(product_list[-1].id + 1, name, price, product_type))
add_product('машина, 1000, транспорт')