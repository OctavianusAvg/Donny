'''
Створіть масив А [1..7] за допомогою генератора випадкових чисел і
виведіть його на екран. Збільште всі його елементи в 2 рази.
Виконав : Канюка Р. 122В
'''
import random
import numpy as np
while True:
    # Рандомна генерація чисел
    while True:
        try:
            A = [random.randint(0,10) for i in range(7)]
            print(A)
            break
        except ValueError :
            print('Введіть число!')
    # Вивід масиву помноженого на 2
    for i in range(len(A)):
        A[i] *= 2
    print(A)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
