'''
Дані про температуру повітря за декаду грудня зберігаються в масиві.
Визначити, скільки раз температура була вище середньої за цю декаду.
Виконав : Канюка Р. 122В
'''
while True:
    Data = list()
    #Ввід данних
    while True:
        try:
            for i in range(0,10):
                Data.append(int(input(f'Данні за {i+1} день декади : ')))
            break
        except ValueError :
            print('Введіть число!')
    #Знаходжень умови
    arth = 0
    itr = 0
    for i in Data:
        arth += i
    arth /= 10
    print(arth)
    for i in range(0,10):
        if(Data[i] > arth):
            itr += 1
    print(f'Було {itr} випадки температури вищої за середню в цій декаді')  
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
