'''
25. Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до
100.
Виконав : Канюка Р. 122В
'''
import random
import numpy as np
while True:
    #Ініціалізація масиву
    X = np.zeros(10)
    for i in range(len(X)):
       X[i] = random.randint(10,100)
    print(X)
    #Знаходження результату
    result = 1
    for i in range(len(X)):
        if (X[i] % 5) == 0 :
            result *= X[i]
    if (result == 1):
        print('Добуток елементів кратних 5 = 0 ')
    else:
        print('Добуток елементів кратних 5 =',result)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
