'''
Створіть масив з 15 цілочисельних елементів і визначте серед них
мінімальне значення.
Виконав : Канюка Р. 122В
'''
while True:
    X = []
    #Ініціалізація масиву
    while True:
            try:
                for i in range(0,15):
                    X.append(int(input(f'Елемент {i+1}: ')))
                break
            except ValueError :
                print('Введіть число!')
    #Знаходження результату
    print('Мінімальне значення : ',min(X))
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
    #

