'''
Створіть цілочисельний масив А [1..15] за допомогою генератора
випадкових чисел з елементами від -15 до 30 і виведіть його на екран. Визначте
найбільший елемент масиву і його індекс.
Виконав : Канюка Р. 122В
'''
import random
import numpy as np
while True:
    # Рандомна генерація чисел
    while True:
        try:
            A = [random.randint(-15,30) for i in range(15)]
            print(A)
            break
        except ValueError :
            print('Введіть число!')
    # заміна відємних чисел
    num = max(A)
    print('Максимум : ' , num ,'З індексом : ', A.index(num)+ 1)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break

