'''
Знайти найбільший елемент з елементів одновимірного масиву, що мають
парний номер. Визначити, чи є він єдиним.
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
            break
        except ValueError :
            print('Введіть число!')
    X = numUserInput(np.empty(n),'Ініціалізація масиву')
    #Знаходження результату
    maxim = 0
    for i in X:
        if i > maxim :
            maxim = i
    print('Максимальне значеня =', maxim)
    if list(X).count(maxim) == 1:
        print('Данний елемент єдиний')
    else : print('Данний елемент не єдиний')
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
