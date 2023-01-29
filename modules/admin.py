
from modules.settings import *
import re


def add_product(message): # get  message.text
    pattern = (r'^([а-яА-Я]+),\s([0-9]+),\s([а-яА-Я]+)$')
    # print(re.match(pattern,str).
    match_result = re.match(pattern,message)
    if match_result:
        name = match_result.group(1)
        price = match_result.group(2)
        product_type = match_result.group(3)
        # Проверяем на то что он подходит под следующий патерн 
        # Название, цена, тип продукта получаем эти значения в переменную
        if list_category:
            for category in list_category:
                if category.name == product_type:
                    break
                else:
                    list_category.append(ProductType(list_category[-1].id + 1, product_type))
                    break
        else:
            list_category.append(ProductType(0, product_type))
        if product_list:
            product_list.append(Product(product_list[-1].id + 1, name, price, product_type))
        else:
            product_list.append(Product(0, name, price, product_type))
    print(product_list)
    print(list_category)
    # Перебираем список product_types_list если тип продукта с таким именем уже есть 
    # то дейтсвий не требуется, иначе
    #  list_category.append(ProductType(list_category[-1].id + 1, type_product))

    # product_list.append(Product(product_list[-1].id + 1, name, price, product_type))
