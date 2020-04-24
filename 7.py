'''
Створіть масив А [1..12] за допомогою генератора випадкових чисел з
елементами від -20 до 10 і виведіть його на екран. Замініть всі від’ємні елементи
масиву числом 0.
Виконав : Канюка Р. 122В
'''
import random
import numpy as np
while True:
    # Рандомна генерація чисел
    while True:
        try:
            A = [random.randint(-20,10) for i in range(12)]
            print(A)
            break
        except ValueError :
            print('Введіть число!')
    # заміна відємних чисел
    for i in range(len(A)):
        if(A[i] < 0):
            A[i] = 0
    print(A)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
