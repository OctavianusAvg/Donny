'''
Знайти суму всіх елементів масиву цілих чисел що задовольняють умові:
остача від ділення на 2 дорівнює 3. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 200 до 300.
Виконав : Канюка Р. 122В
'''
import random
import numpy as np
while True:
    #Ініціалізація масиву
    X = np.zeros(20)
    for i in range(len(X)):
       X[i] = random.randint(200,300)
    print(X)
    #Знаходження результату
    # Парні елементи матимуть не парний індекс. Тому:
    summ = 0
    for i in range(len(X)):
    #Нажаль ,програма не змогла знайти таких елементів.
        if(X[i] % 2 == 3):
            summ += X[i]
    print('Сумма заданих елемениів =', summ)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break