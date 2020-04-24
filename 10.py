'''
Дані про температуру повітря за декаду листопада зберігаються в масиві.
Визначити, скільки разів температура опускалася нижче -10 градусів.
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
    itr = 0
    for i in range(0,10):
        if(Data[i] < -10):
            itr += 1
    print(f'Було {itr} випадки температура за декаду нижнчої за -10 ')
            
            
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
