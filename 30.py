'''
Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які розташовані за першим по порядку мінімальним елементом.
Виконав : Канюка Р. 122В
'''
import numpy as np
import random
#Методи - заготовки
def arith(arr,pos):
    '''Метод знаходження середнього арифметичне для масивів після pos.

    Приймає масив дійсних чисел та pos
    і повертає середне арифметчне
    '''
    result = 0
    for i in range(pos + 1,len(arr)):
        result += arr[i]
    return (result / (len(arr)- pos))
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
    #Знаходження мінімального елемента
    min_el = T.tolist().index(min(T))
    print('Середне арифметичне після мінімума :',arith(T,min_el))
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
