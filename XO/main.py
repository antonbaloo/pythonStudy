import pvp as pp


def menu():
    print('Крестики нолики')
    print('[1] Игрок 1 против Игрок 2')
    print('[2] Игрок против Компьютер')
    print('[3] СТатистика')
    print('[0] Выход')

# def fieldsize(size=0):
#     print("""Выберите размер поля:
#           '[1] 3 на 3'
#           '[2] 4 на 4'
#           '[3] 5 на 5'
#           '[4] 6 на 6'""")
#     print('')
#     item = int(input('Введите выбраный пункт:'))
#     if item == 1:
#         return 3
#     elif item == 2:
#         return 4
#     elif item == 3:
#         return 5
#     elif item == 4:
#         return 6


while True:
    menu()
    print('')
    option = int(input('Выберите пункт меню (от 1 до 3):'))
    if option == 1:
        print('')
        print('Вы выбрали пункт "Игрок 1 против Игрок 2"')
        pp.startpvp()
    elif option == 2:
        print('')
        print('Вы выбрали пункт "Игрок против Компьютер"')
        # break
    elif option == 3:
        print('')
        print('Статистика')
        print('')
        # break
    elif option == 0:
        print('~~~~~~~~~~~~~~~')
        print('Спасибо за игру')
        print('~~~~~~~~~~~~~~~')
        break
    else:
        print()
        print('!!!Неверный пункт!!!')
        print()
