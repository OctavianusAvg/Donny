'''
Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
Заповнення масиву здійснити випадковими числами від 5 до 500.
Виконав : Канюка Р. 122В
'''
import numpy as np
import random
while True:
    #Ініціалізація масиву
    X = np.zeros(10)
    for i in range(len(X)):
       X[i] = random.randint(5,500)
    print(X)
    #Знаходження результату
    result = 1
    for i in range(len(X)):
        # Якщо ,число ділиться на 9 ,то й ділиться на 3.
        if (X[i] % 9) == 0:
            result *= X[i]
    if (result == 1):
        print('Добуток елементів кратних 9 і 3  = 0 ')
    else:
        print('Добуток елементів кратних 9 і 3  =',result)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
