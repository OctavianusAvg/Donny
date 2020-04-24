'''
Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком,
починаючи з останнього.
Виконав : Канюка Р. 122В
'''
import numpy as np
while True:
    X = list()
    for i in range(5):
        X.append(input(f'Введіть {i+1} прізвище : '))
    for i in range(4 , -1 , -1):
        print(X[i])
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
