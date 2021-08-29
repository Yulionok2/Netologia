# Разработать приложение для определения знака зодиака по дате рождения.

month=str(input('Введите месяц: '))
number=int(input('Введите число: '))

if month=='январь':
  if number<=20:
    print('Козерог')
  else:
    print('Водолей')
elif month=='февраль':
  if number<=18:
    print('Водолей')
  else:
    print('Рыбы')
elif month=='март':
  if number<=20:
    print('Рыбы')
  else:
    print('Овен')
elif month=='апрель':
  if number<=20:
    print('Овен')
  else:
    print('Телец')
elif month=='май':
  if number<=20:
    print('Телец')
  else:
    print('Близнецы')
elif month=='июнь':
  if number<=21:
    print('Близнецы')
  else:
    print('Рак')
elif month=='июль':
  if number<=22:
    print('Рак')
  else:
    print('Лев')
elif month=='август':
  if number<=23:
    print('Лев')
  else:
    print('Дева')
elif month=='сентябрь':
  if number<=23:
    print('Дева')
  else:
    print('Весы')
elif month=='октябрь':
  if number<=23:
    print('Весы')
  else:
    print('Скорпион')
elif month=='ноябрь':
  if number<=22:
    print('Скорпион')
  else:
    print('Стрелец')
elif month=='декабрь':
  if number<=21:
    print('Стрелец')
  else:
    print('Козерог')
