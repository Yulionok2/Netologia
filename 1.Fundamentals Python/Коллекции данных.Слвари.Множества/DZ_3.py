# Дан список поисковых запросов. Получить распределение количества слов в них. Т.е. поисковых запросов из 
# одного - слова 5%, из двух - 7%, из трех - 3% и т.д.

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

dict_1 = {}
for query in queries:
  words = query.split()
  if len(words) in dict_1.keys():
    dict_1[len(words)] += 1 
  else:
    dict_1.update({len(words): 1})
for key, value in dict_1.items():
  percent = (value / len(queries) * 100)
  print(f'Поисковых запросов из {key} слова: {percent}%')

y = dict()
for words in queries:
  x = words.split()
  if len(x) in y.keys():
    y[len(x)] = y[len(x)] + 1 
  else:
    y[len(x)] = 1
for key, value in y.items():
  percent = (value / len(queries) * 100)
  print(f'Поисковых запросов из {key} слов: {percent} %')