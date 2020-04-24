'''
Знайти кількість парних елементів одновимірного масиву до першого
зустрінутого числа рівного наперед заданому числу а.
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
                n = int(input('Введіть кількість елеменетів в масиві : '))
                a = int(input('Введіть число а : '))
                break
            except ValueError :
                print('Введіть число!')
    T = numUserInput(np.empty(n),'Ініціалізація масиву')
    #Знаходження результату
    result = 0
    for i in T:
        if i % 2 == 0:
            result += 1
        if i == a: break
    print('Кількість парних елементів до числа а :',result)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
