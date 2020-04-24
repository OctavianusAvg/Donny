'''
Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
від 50 до 100.
Виконав : Канюка Р. 122В
'''
import random
import numpy as np
while True:
    #Ініціалізація масиву
    X = np.zeros(10)
    while True:
            try:
                keyword = float(input('Введіть задане число : '))
                break
            except ValueError :
                print('Введіть число!')
    for i in range(len(X)):
       X[i] = random.randint(50,100)
    print(X)
    #Знаходження результату
    result = 1
    for i in range(len(X)):
        if X[i] < keyword :
            result *= X[i]
    if (result == 1):
        print('Данних елементів не знайдено')
    else:
        print(f'Добуток елементів менших за {keyword} = {result}')
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
