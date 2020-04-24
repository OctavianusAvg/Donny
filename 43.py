'''
Задано два натуральних числа a і b. Змінній w привласнити значення
істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
і не кратний b.
Виконав : Канюка Р. 122В
'''
import numpy as np
import random
def numUserInput(arr, message):
    '''Ініціалзіцая масиву дійсних чисел користувачем.

    Приймає масив та загальне повідомлення.
    '''
    print(message)
    while True:
        try:
            for i in range(len(arr)):
                arr[i] = int(input(f'Введіть {i+1} елемент : '))
            break
        except ValueError :
            print('Введіть число!')
    return arr
while True:
    #Ініціалізація масиву
    while True:
        try:
            n = int(input(f'Введіть кількість елементів: '))
            a = int(input(f'Введіть число a: '))
            b = int(input(f'Введіть число b: '))
            break
        except ValueError :
            print('Введіть число!')
    X = numUserInput(np.empty(n),'Ініціалізація масиву')
    #Знаходження результату
    w = False
    for i in X:
        if i % a == 0 and i % b:
            w = True
    print('w =',w)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
