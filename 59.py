'''
59.Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних
чисел в ньому.
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
    count = len(set(X))
    print(count)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
