# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

user_float_number = input('Введите число, программа посчитает сумму всех его цифр: ')
sum_of_digits_in_number = 0

for i in user_float_number:
    if i !='-' and i !='.' and i != ',':
        sum_of_digits_in_number = sum_of_digits_in_number + int(i)
print(f'Сумма цифр во введенном числе равна: {sum_of_digits_in_number}')

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial
def f(x):
    return ((x == 1) and 1) or x * factorial(x - 1)

user_number1 = int(input('Введите число, программа покажет набор произведений чисел от 1 до введенного числа: '))
result = list(f(i) for i in range(1, user_number1 + 1))
print(f'Набор произведений чисел от 1 до {user_number1}:')
print(result)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.

import random

user_number2 = int(input('Введите число: '))
result_list = []

for i in range(user_number2):
    result_list.append(random.randint(-user_number2, user_number2))

print('Получился список: ')
print(result_list)

first_number_position = int(input(f'Введите индекс первого перемножаемого элемента (от 0 до {user_number2 - 1}): '))
second_number_position = int(input(f'Введите индекс второго перемножаемого элемента (от 0 до {user_number2 - 1}): '))

multiplication_result = result_list[first_number_position] * result_list[second_number_position]
print(f'Перемножаемые числа {result_list[first_number_position]} и {result_list[second_number_position]}')
print(f'Результат перемножения: {multiplication_result}')

# Реализуйте алгоритм перемешивания списка.

import random

user_list = input('Введите элементы списка через пробел: ').split(' ')
print('Исходный список: ')
print(user_list)
print()
random.shuffle(user_list)
print('Перемешенный список: ')
print(user_list)

# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму

user_num_for_subsequence = int(input('Введите число: '))
subsequence_list = []
start_num = 1
while start_num <= user_num_for_subsequence:
    list.append(subsequence_list, round((1 + 1 / start_num) ** start_num,2))
    start_num += 1
subsequence_list_sum_of_elements = 0
for element in subsequence_list:
    subsequence_list_sum_of_elements += element
print('Получена последовательность чисел: ')
print(subsequence_list)
print('Сумма всех элементов в данной последовательности равна: ')
print(subsequence_list_sum_of_elements)