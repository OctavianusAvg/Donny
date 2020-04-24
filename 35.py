'''
Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
спаданню.
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
    i = 0
    while i != n - 1:
        print(i , '/ ' , i != n )
        if(X[i] >= X[i + 1]):
            i += 1
        else :
            print('Масив не відсортований')
            break
    if(i == n - 1): print('Масив відсортований')
    
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
