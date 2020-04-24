'''
Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
починаються з певної букви, яка вводиться з клавіатури.
Виконав : Канюка Р. 122В
'''
import numpy as np
while True:
    X = list()
    #Ініціалізація масиву
    for i in range(5):
        X.append(input(f'Введіть {i+1} прізвище : '))
    keyword = input(f'Введіть шукану букву : ')
    for i in range(5):
        if X[i][0] == keyword :
            print(X[i])
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
