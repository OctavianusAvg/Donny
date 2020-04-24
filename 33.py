'''
Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
Виконав : Канюка Р. 122В
'''
import numpy as np
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
    arr = numUserInput(np.empty(20),'Ініціалізація масиву')
    #Знаходження результату
    result = 1
    for i in arr:
        if(i != 0) :
            result *= i
    if (result == 1):
        print('Такі елементи відсутні')
    else:
        print('Добуток елементів =',result)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break


        
