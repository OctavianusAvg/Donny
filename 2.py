'''
Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
екран значення коріння і квадратів кожного з елементів масиву.
Виконав : Канюка Р. 122В
'''
import math
import numpy as np
while True :
    X = np.zeros(5)
    # ініціалізація масиву
    while True:
        try:
            for i in range(5):
                X[i] =int(input(f'Введіть елемент {i+1} : '))
            break
        except ValueError :
            print('Введіть число!')
    # вивід квадрата і кореня
    for i in range(5):
        print(f'Eлемент {i+1} \nквадтрат :', pow(X[i],2), '\nкорінь :',math.sqrt(X[i]))
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
    
