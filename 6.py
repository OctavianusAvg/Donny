'''
Створіть масив А [1..8] за допомогою генератора випадкових чисел з
елементами від -10 до 10 і виведіть його на екран. Підрахуйте кількість від’ємних
елементів масиву.
Виконав : Канюка Р. 122В
'''
import random
import numpy as np
while True:
    # Рандомна генерація чисел
    while True:
        try:
            A = [random.randint(-10,10) for i in range(8)]
            print(A)
            break
        except ValueError :
            print('Введіть число!')
    # Вивід кількості відємних чисел
    itr = 0
    for i in range(len(A)):
        if A[i] < 0 :
            itr += 1
    print('Кількість відємних чисел :',itr)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
