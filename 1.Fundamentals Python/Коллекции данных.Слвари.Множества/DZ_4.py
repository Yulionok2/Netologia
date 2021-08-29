# Дана статистика рекламных каналов по объемам продаж. Напишите скрипт, который возвращает название канала с 
# максимальным объемом. Т.е. в данном примере скрипт должен возвращать 'yandex'.

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

volume_of_sales = ''
for companies in stats.keys():
  if stats[companies] > stats.get(volume_of_sales,0):
    volume_of_sales = companies
print(volume_of_sales)