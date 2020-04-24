'''
60.Дан одновимірний масив з 10 цілих чисел. Підрахуйте найбільше число
однакових чисел, що йдуть підряд в ньому.
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
    n = len(X)
    for i in range(n):
        temp = 1
        for j in range(i+1, n):
            if X[i] == X[j]:
                temp += 1
            else :break
        if temp > count :
            count = temp
    print('Кількість =',count)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
