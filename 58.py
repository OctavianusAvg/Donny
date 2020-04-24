'''
58. Дан одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому
повторюється найчастіше число.
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
    L = list(X)
    result = 0
    for i in range(len(L)):
        p =  L.count(L[i])
        if p > result :
            result = p
            index = i
    print(f'Найчастіше число {L[index]} зустрічається {result} рази ')
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
