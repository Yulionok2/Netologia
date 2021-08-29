# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы 
# будем готовить
# get_shop_list_by_dishes(dishes, person_count)

# На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для 
# такого вызова
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

from DZ_1 import dict_cook_book

def get_shop_list_by_dishes(dishes, person_count):
    file_txt = dict_cook_book('cookbook.txt')
    dish_person = {}
    for dish in dishes:
        for item in (file_txt[dish]):
            items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*person_count})])
            dish_person += items_list
    print(f"На {person_count} персон нам необходимо купить:")
    print(dish_person)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)

{
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}
