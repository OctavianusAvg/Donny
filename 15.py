'''
Знайти суму парних елементів масиву цілих чисел. Розмірність масиву -
20. Заповнення масиву здійснити випадковими числами від 100 до 200.
Виконав : Канюка Р. 122В
'''
import random
import numpy as np
while True:
    #Ініціалізація масиву
    X = np.zeros(20)
    for i in range(len(X)):
       X[i] = random.randint(100,200)
    print(X)
    #Знаходження результату
    # Парні елементи матимуть не парний індекс. Тому:
    summ = 0
    for i in range(1,20,2):
        summ += X[i]
    print('Сумма парних елементів =', summ)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
