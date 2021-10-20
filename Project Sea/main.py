
def menu():
    print('МОРСКОЙ БОЙ')
    print('[1] Игрок 1 против Игрок 2')
    print('[2] Игрок против Компьютер')
    print('[3] СТатистика')
    print('[0] Выход')

def fieldsize(size=0):
    print("""Выберите размер поля:
          '[1] 10 на 10 '
          '[2] 12 на 12'
          '[3] 15 на 15""")
    print('')
    item = int(input('Введите выбраный пункт:'))
    if item == 1:
        return 10
    elif item == 2:
        return 12
    elif item == 3:
        return 15

menu()
print('')
option = int(input('Выберите пункт меню (от 1 до 3):'))
if option == 1:
    print('Вы выбрали пункт "Игрок 1 против Игрок 2"')
    size = fieldsize()
    print('ВЫ выбрали поле размером:{}'.format(size))

elif option == 2:
    print('Вы выбрали пункт "Игрок против Компьютер"')
    # break
elif option == 3:
    print('Статистика')
    # break
elif option == 0:
    print('Спасибо за игру')
else:
    print()
    print('!!!Неверный пункт!!!')
    print()



