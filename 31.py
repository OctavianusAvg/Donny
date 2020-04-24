'''
Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які потрапляють в інтервал від -2 до 10.
Виконав : Канюка Р. 122В
'''
import numpy as np
#Методи - заготовки
def arith(arr):
    '''Метод знаходження середнього арифметичне для масивів.

    Приймає масив дійсних чисел
    і повертає середне арифметчне
    '''
    result = 0
    n = len(arr)
    for i in range(len(arr)):
        if arr[i] > -2 and arr[i] < 10: 
            result += arr[i]
        else:
            n -= 1
    print(result)
    print(n)
    return (result / n)
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
    T = numUserInput(np.empty(n),'Ініціалізація масиву')
    #Знаходження результату
    print('Середне арифметичне для заданого випадку :',arith(T))
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
