'''
Дан одновимірний масив а. Сформувати новий масив, який складається
тільки з тих елементів масиву а, які перевищують свій номер на 10. Якщо таких
елементів немає, то видати повідомлення.
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
    A = list()
    for i in range(len(X)):
        if (X[i] - i) > 10:
            A.append(X[i])
    if len(A) != 0 :
        print(A)
    else :
        print('Данних елементів не знайдено')
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
