'''
Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.
Виконав : Канюка Р. 122В
'''
import numpy as np
import random
while True:
    #Ініціалізація масиву
    X = np.zeros(15)
    for i in range(len(X)):
       X[i] = random.randint(10,50)
    print(X)
    #Знаходження результату
    result = 1
    for i in range(len(X)):
        if (X[i] % 7) == 0 :
            result *= X[i]
    if (result == 1):
        print('Добуток елементів кратних 7 = 0 ')
    else:
        print('Добуток елементів кратних 7 =',result)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
