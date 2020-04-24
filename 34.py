'''
Дано два лінійних масиву однакової розмірності. Скласти третій масив з
добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.
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
    #Знаходження результату
    arr_1 = numUserInput(np.empty(n),'Ініціалізація першого масиву')
    arr_2 = numUserInput(np.empty(n),'Ініціалізація другого масиву')
    arr_3 = np.empty(n)
    for i in range(n):
        arr_3[i] =  arr_2[i] * arr_1[i]
    print('Кінцевий масив :',arr_3)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
