# Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек/
# Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и 
# познакомим людей с одинаковыми индексами после сортировки! "Познакомить" пары нам поможет функция zip, 
# а в цикле распакуем zip-объект/

boys = ['Peter', 'Alex', 'John', 'Artur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys.sort()
girls.sort()

# Вариант решения 1
print('Идеальные пары:')
if len(boys)==len(girls):
  for couple in zip(boys, girls):
    print(f'{couple[0]} и ', end = '')
    print(couple[1])
else:
  print('Кто-то может остаться без пары')

# Вариант решения 2
if len(boys)==len(girls):
  print('Идеальные пары:')
  for name_1, name_2 in zip(boys, girls):
    print(f'{name_1} и {name_2}')
else:
  print('Кто-то может остаться без пары')