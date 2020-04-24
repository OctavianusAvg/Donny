'''
Знайти суму всіх елементів масиву дійсних чисел, більших за задане
число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
від 50 до 100.
Виконав : Канюка Р. 122В
'''
import random
import numpy as np
while True:
    #Ініціалізація масиву
    X = np.zeros(20)
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
    # Парні елементи матимуть не парний індекс. Тому:
    summ = 0
    for i in range(len(X)):
        if X[i] > keyword:
            summ += X[i]
    print(f'Сумма елементів більших за {keyword} = {summ}')
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
