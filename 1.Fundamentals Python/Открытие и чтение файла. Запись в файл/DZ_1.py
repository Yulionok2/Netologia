# Необходимо написать программу для кулинарной книги.
# Должен получится следующий словарь

def dict_cook_book(file_name):
    cook_book = {}
    with open(file_name, encoding = 'utf-8') as file:
        for line_ in file:
            dish_name = line_.strip()
            line = file.readline()
            number = int(line)
            list_of_ingridient = []
            for ingridient in range(number):
                dict_1 = {}
                lines = file.readline().strip().split(' | ')
                for item in lines:
                    dict_1['ingredient_name'] = lines[0]
                    dict_1['quantity'] = lines[1]
                    dict_1['measure'] = lines[2]
                list_of_ingridient.append(dict_1)
                menu = {dish_name: list_of_ingridient}
                cook_book.update(menu)
            file.readline()

cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
