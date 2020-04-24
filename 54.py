'''
Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
однаковими значеннями.
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
    X = numUserInput(np.empty(20),'Ініціалізація масиву')
    #Знаходження результату
    if len(set(X)) < 20 :
        print('Данні елементи присутні')
    else :
        print('Данні елементи відсутні')
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
