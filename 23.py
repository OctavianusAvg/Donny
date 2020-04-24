'''
Знайти суму всіх елементів масиву цілих чисел, які менше середнього
арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 150 до 300.
Виконав : Канюка Р. 122В
'''
import random
import numpy as np
while True:
    #Ініціалізація масиву
    X = np.zeros(20)
    for i in range(len(X)):
       X[i] = random.randint(150,300)
    print(X)
    #Знаходження результату
    arth = 0
    for i in X:
        arth += i
    arth /= len(X)
    print(arth)
    summ = 0
    for i in X:
        if i < arth:
            summ += i
    print('Сумма заданих елемениів =', summ)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
