'''
27. Лінійний масив містить відомості про кількість опадів, що випали за
кожен з 12 місяців одного року. Складіть програму, що визначає загальну кількість
опадів протягом цього року, середньомісячну кількість опадів, кількість посушливих
місяців (коли кількість опадів було менше 30 мм), найпосушливіший місяць року.
Виконав : Канюка Р. 122В
'''
import numpy as np
import random
def userInput(arr, message, numeric):
    '''Ініціалзіцая масиву користувачем.

    Приймає масив , загальне повідомлення , та флажок
    ,що визначає чи є тип елементів масиву дійсними числами.
    '''
    print(message)
    if numeric :
        while True:
            try:
                for i in range(len(arr)):
                    arr[i] = int(input(f'Введіть данні за {i+1} місяць : '))
                break
            
            except ValueError :
                print('Введіть число!')
        return arr
    else :
        for i in range(len(arr)):
            arr[i] = input(f'Введіть данні за {i+1} місяць : ')
        return arr
    
while True:
    #Ініціалізація масиву
    T = userInput(np.empty(12),'Введіть кількість опадів за рік', True)
    #Знаходження результату
    print('Загальна кількість опадів :',T.sum())
    print('Середня арифметична кількість опадів :',T.mean())
    summ = 0
    for i in T:
        if i < 30:
            summ += 1
    print('Кільскість посушливих місяців :', summ )
    print('Найпосушливішим місяцем року був ', (T.tolist().index(min(T))+ 1))
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
