'''
Дані про температуру повітря і кількості опадів за декаду квітня
зберігаються в масивах. Визначити кількість опадів, що випали у вигляді дощу і у
вигляді снігу за цю декаду.
Виконав : Канюка Р. 122В
'''
import numpy as np
import random
def numUserInputSpecial(arr, message):
    '''Ініціалзіцая масиву дійсних чисел користувачем.

    Приймає масив та загальне повідомлення.
    '''
    print(message)
    while True:
        try:
            for i in range(len(arr[0])):
                arr[0][i] = input(f'Введіть температура повітря за {i+1} день : ')
                arr[1][i] = int(input(f'Введіть кількість опадів за {i+1} день : '))
            break
        except ValueError :
            print('Введіть число!')
    return arr
while True:
    #Ініціалізація масиву
    X = numUserInputSpecial(np.empty([2,10]),'Масив данних по вітру за декаду квітня')
    #Знаходження результату
    snow = 0
    rain = 0
    for i in range(len(X[0])):
        if X[0][i] >= 0 :
            rain += X[1][i]
        else :
            snow += X[1][i]
    print('Опади у вигляду снігу :', snow)
    print('Опади у вигляду дощу :', rain)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
