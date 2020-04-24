'''
Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8
одночасно. Розмірність масиву - 30. Заповнення масиву здійснити випадковими
числами від 500 до 1000.
Виконав : Канюка Р. 122В
'''
import random
import numpy as np
while True:
    #Ініціалізація масиву
    X = np.zeros(30)
    for i in range(len(X)):
       X[i] = random.randint(500,1000)
    print(X)
    #Знаходження результату
    summ = 0
    for i in X:
        if i % 5 == 0 and i % 8 == 0:
            summ += i
    print('Сумма заданих елемениів =', summ)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
