'''
Перетин даху має форму півкола з радіусом R м. Сформувати таблицю,
яка містить довжини опор, які встановлюються через кожні R / 5 м.
Виконав : Канюка Р. 122В
'''
import math
import numpy as np
while True:
    #Ініціалізація масиву
    while True:
        try:
            R = int(input(f'Введіть радіус: '))
            break
        except ValueError :
            print('Введіть число!')
    # Довжина масиву 11 тому ,що півкола можна поділити
    # на 10 проможків ,де буде 11 опор за умови R/ 5 м.
    X = np.empty(11)
    for i in range(6):
        print(i)
        X[i] = R * math.sqrt(25 - pow(5 - i , 2))
        X[(-1 - i)] = X[i]
        print(X[i])
    #Знаходження результату
    print('Опора  Довжина')
    for i in range(len(X)):
        print(f'{i+1}     {X[i]}')
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
