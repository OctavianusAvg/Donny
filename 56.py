'''
56.Якщо в одновимірному масиві є три поспіль однакових елемента, то
змінній r привласнити значення істина.
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
    X = numUserInput(np.empty(10),'Ініціалізація масиву')
    #Знаходження результату
    count = 0
    r = False
    n = len(X)
    for i in range(n):
        temp = 1
        for j in range(i+1, n):
            if X[i] == X[j]:
                temp += 1
            else :break
        if temp >= 3:
            r = True
    print('r =',r)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
