# Пользователь вводит длину и ширину фигуры.Программа выводит их периметр и площадь.

square=int(input("Введите длину стороны квадрата:"))
P=square*4
S=square**2
print("Вывод: ")
print("Периметр:", P)
print("Площадь:", S)

rectangle_a=int(input("Введите длину прямоугольника:"))
rectangle_b=int(input("Введите ширину прямоугольника:"))
P=(rectangle_a+rectangle_b)*2
S=rectangle_a*rectangle_b
print("Вывод: ")
print("Периметр:", P)
print("Площадь:", S)