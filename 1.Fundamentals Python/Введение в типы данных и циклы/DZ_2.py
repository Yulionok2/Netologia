# Имеется структура данных cook_book, в которой хранится информация об ингредиентах блюд и их количестве 
# в расчете на одну порцию. и переменная, в которой хранится количество людей, на которых необходимо 
# приготовить данные блюда. Необходимо вывести пользователю список покупок необходимого количества 
# ингредиентов для приготовления блюд на определенное число персон/

cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',  
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],  
      ]
  ]
]

person = int(input())

for dish in cook_book:
  print(f'{dish[0]}: ')
  for ingredients, weight, measure in dish[1]:
    print(f'{ingredients}, {int(weight) * person} {measure}')
  print()

