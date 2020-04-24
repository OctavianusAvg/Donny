'''
Змінній t привласнити значення істина, якщо в одновимірному масиві є
хоча б одне від’ємне і парне число.
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
    while True:
            try:
                n = int(input('Введіть кількість елеменетів в масиві : '))
                break
            except ValueError :
                print('Введіть число!')
    arr = numUserInput(np.empty(n),'Ініціалізація масиву')
    #Знаходження результату
    t = False
    for i in arr:
        if(i < 0 and i % 2 == 0):
            t = True
            break
    print('t =',t)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
