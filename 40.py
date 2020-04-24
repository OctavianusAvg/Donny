'''
Обчислити суму парних елементів одновимірного масиву до першого
зустрінутого нульового елемента.
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
    summ = 0
    i = 0
    while i != n:
        if X[i] != 0:
            summ += X[i]
            i += 1
        else : break
    print('Сумма =',summ)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
