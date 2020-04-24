'''
В масиві X (1: n) кожен елемент рівний 0, 1 або 5. Переставити елементи
масиву так, щоб спочатку розташовувалися всі нулі, потім все одиниці, а потім всі
п'ятірки. Додаткового масиву не заводити.
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
            n = int(input(f'Введіть кількість елементів: '))
            break
        except ValueError :
            print('Введіть число!')
    X = numUserInput(np.empty(n),'Ініціалізація масиву')
    #Знаходження результату
    print(np.sort(X))
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
