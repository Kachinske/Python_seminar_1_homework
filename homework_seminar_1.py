# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

user_day_of_week = int(input('Введите день недели: '))
while 8 < user_day_of_week > 0:
    user_day_of_week = int(input('Подумай еще, ведь в неделе 7 дней.\nВведите день недели: '))
else:
    if 0 < user_day_of_week < 6:
        print(user_day_of_week,' -> будний день')
    else:
        print(user_day_of_week,' -> выходной день')

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

user_coordinate_x = int(input("Введите координату по оси x отличную от 0: "))
user_coordinate_y = int(input("Введите координату по оси y отличную от 0: "))
if user_coordinate_x == 0:
    user_coordinate_x = int(input("Введите координату по оси x отличную от 0: "))
if user_coordinate_y == 0:
    user_coordinate_y = int(input("Введите координату по оси y отличную от 0: "))
if user_coordinate_x > 0 and user_coordinate_y > 0:
    print(f'Координаты ({user_coordinate_x},{user_coordinate_y}) находятся в четверти № 1')
elif user_coordinate_x < 0 and user_coordinate_y > 0:
    print(f'Координаты ({user_coordinate_x},{user_coordinate_y}) находятся в четверти № 2')
elif user_coordinate_x < 0 and user_coordinate_y < 0:
    print(f'Координаты ({user_coordinate_x},{user_coordinate_y}) находятся в четверти № 3')
else:
    print(f'Координаты ({user_coordinate_x},{user_coordinate_y}) находятся в четверти № 4')

# 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

user_quarter_number = int(input("Введите номер четверти в плоскости координат: "))
while user_quarter_number < 1 or user_quarter_number > 4:
    user_quarter_number = int(input("Данной четверти не существует.\nВведите номер четверти в плоскости координат: "))
if user_quarter_number == 1:
    print(f'В четверти {user_quarter_number} для x и y доступен следующий диапазон значений: \nx: 0  -> ထ\ny: 0  -> ထ')
if user_quarter_number == 2:
    print(f'В четверти {user_quarter_number} для x и y доступен следующий диапазон значений: \nx: -ထ  -> 0\ny: 0  -> ထ')
if user_quarter_number == 3:
    print(f'В четверти {user_quarter_number} для x и y доступен следующий диапазон значений: \nx: -ထ  -> 0\ny: -ထ  -> 0')
if user_quarter_number == 4:
    print(f'В четверти {user_quarter_number} для x и y доступен следующий диапазон значений: \nx: 0  -> ထ\ny: -ထ  -> 0')

# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def distance_between_two_points_2d(x1,y1,x2,y2):
    result = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5,2)
    return result

first_point_coordinate_x = int(input("Введите координату первой точки по оси X: "))
first_point_coordinate_y = int(input("Введите координату первой точки по оси Y: "))
second_point_coordinate_x = int(input("Введите координату второй точки по оси X: "))
second_point_coordinate_y = int(input("Введите координату второй точки по оси Y: "))
distance = distance_between_two_points_2d(first_point_coordinate_x,first_point_coordinate_y,second_point_coordinate_x,second_point_coordinate_y)
print(f'Расстояние между точками ({first_point_coordinate_x},{first_point_coordinate_y}) и ({second_point_coordinate_x},{second_point_coordinate_y}) -> {distance}')