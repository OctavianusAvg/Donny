'''Введіть з клавіатури в масив п'ять цілочисельних значень.
Виведіть їх в один рядок через кому.
Отримайте для масиву середнє арифметичне.
Виконав : Канюка Р. 122В
'''
import numpy as np
while True:
    arr = np.zeros(5)
    arthsum = 0
    # ініціалізація масиву
    while True:
        try:
            for i in range(5):
                arr[i] = int(input(f'Введіть елемент {i+1} : '))
            break
        except ValueError :
            print('Введіть число!')
    # вивід масиву та середього арифмет.
    for i in range(5):
        print(arr[i],end = ', ')
        arthsum += arr[i]
    print('\nСереднє арифметичне :',(arthsum / 2))
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
        

    
    
