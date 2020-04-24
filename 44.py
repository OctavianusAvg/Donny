'''
Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
своїм номером і при цьому кратні 3.
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
    for i in range(len(X)):
    # Номер елемента на 1 більщий за його індекс ,тому i + 1
        if i+1 == X[i] and X[i] % 3 == 0:
            summ += 1
    print('Кількість данних елементів =',summ)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
