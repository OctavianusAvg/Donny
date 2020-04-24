'''
Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність
масиву - 10. Заповнення масиву здійснити за допомогою клавіатури.
Виконав : Канюка Р. 122В
'''
import random
import numpy as np
while True:

    #Ініціалізація масиву
    X = np.zeros(10)
    while True:
        try:
            for i in range(len(X)):
                X[i] = int(input(f'Введіть {i+1} елемент : '))
            print(X)   
            break
        except ValueError :
            print('Введіть ціле число!')
    #Знаходження результату
    result = 1
    for i in range(len(X)):
        if X[i] < 0 :
            result *= X[i]
    if (result == 1):
        print('Такі елементи відсутні')
    else:
        print('Добуток елементів менших 0 =',result)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
