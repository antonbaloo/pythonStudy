import statistic


def fieldsize():
    print("""Выберите размер поля:
          '[1] 3 на 3'
          '[2] 4 на 4'
          '[3] 5 на 5'
          '[4] 6 на 6'""")
    print('')
    item = int(input('Введите выбраный пункт:'))
    if item == 1:
        return 3
    elif item == 2:
        return 4
    elif item == 3:
        return 5
    elif item == 4:
        return 6


def field(size):
    print('~~~~~~~~~~~~~')
    print('Игровое поле')
    print('')
    count = 10
    global a
    global b
    a = []
    for row in range(size):
        b = []
        for col in range(size):
            count += 1
            b.append(['{:02.0f}'.format(count)])
        a.append(b)
        if size == 3:
            count += 7
        elif size == 4:
            count += 6
        elif size == 5:
            count += 5
        elif size == 6:
            count += 4
    for row in a:
        print(row)
    return a


def showfield():
    for row in a:
        print(row)


def choiseplr():
    print('КТо будет первый ходить? ')
    print('[1] Игрок 1 (Х)')
    print('[2] Игрок 2 (0)')
    global choise
    while True:
        plr = int(input('Выберите пункт меню: '))
        if plr == 1:
            print('Игрок 1 (Х) ходит первым ')
            choise = 1
            return choise
        elif plr == 2:
            print('Игрок 2 (0) ходит первым ')
            choise = 2
            return choise
        else:
            print('Неправильный пункт меню. Попробуйте ещё раз')
            continue


def plrmove(row, col):
    a[row - 1][col - 1] = plrtag


# def plr1move(row,col):
#     a[row-1][col-1] = plr1tag


# def plr2move(row,col):
#     a[row-1][col-1] = plr2tag


def checkmove(size, row, col):
    if (row > size) or (row < 1) or (col > size) or (col < 1):
        print('Неверное число! Числа должны быть между 1 и {}'.format(size))
        return False
    else:
        return True


def istaken(row, col):
    if a[row - 1][col - 1] == ['X'] or a[row - 1][col - 1] == ['O']:
        print('Эта ячейка уже занята')
        return True


def changeplayer(choise, counter):
    global plrtag
    global player
    global plrscale
    if choise == 1 and counter == 0:
        plrtag = ['X']
        player = 'Игрок 1'
        plrscale = 1
        print(" Ходит Игрок 1")
        return plrtag, player, plrscale
    elif choise == 1 and counter > 0:
        if counter % 2 != 0:
            plrtag = ['O']
            player = 'Игрок 2'
            plrscale = 2
            print(" Ходит Игрок 2")
            return plrtag, player, plrscale
        else:
            plrtag = ['X']
            player = 'Игрок 1'
            plrscale = 1
            print(" Ходит Игрок 1")
            return plrtag, player, plrscale

    elif choise == 2 and counter == 0:
        plrtag = ['O']
        player = 'Игрок 2'
        plrscale = 2
        print(" Ходит Игрок 2")
        return plrtag, player, plrscale
    elif choise == 2 and counter > 0:
        if counter % 2 != 0:
            plrtag = ['X']
            player = 'Игрок 1'
            plrscale = 1
            print(" Ходит Игрок 1")
            return plrtag, player, plrscale
        else:
            plrtag = ['O']
            player = 'Игрок 2'
            plrscale = 2
            print(" Ходит Игрок 2")
            return plrtag, player, plrscale


def iswin(player, plrtag, a, size):
    if checkrow(player, plrtag, a, size): return True
    if checkcol(player, plrtag, a, size): return True
    if checkdiag(player, plrtag, a, size): return True
    return False


def checkrow(player, plrtag, a, size):
    for row in a:
        hit = 0
        for col in row:
            if col == plrtag:
                hit += 1
                if hit == size:
                    return True


def checkcol(player, plrtag, a, size):
    i = 1
    while True:
        hit = 0
        for col in a:
            for row in col[i - 1:i]:
                if row == plrtag:
                    hit += 1
                    if hit == size:
                        return True
        i += 1
        if i > size:
            break


def checkdiag(player, plrtag, a, size):
    hit = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (i == j) or (i == ((size - 1) - j)):
                if a[i][j] == plrtag:
                    hit += 1
                    if hit == size:
                        return True



def startpvp():
    # Выбор размера поля и его вывод на экран
    size = fieldsize()
    field(size)

    # Выбор кто будет ходить первым
    print('')
    choiseplr()
    print('')

    # Счётчик ходов (для случая Ничьи)
    counter = 0
    x = 'X'
    o = 'O'
    while True:
        print('')

        # Функция смены игрока

        changeplayer(choise, counter)

        # Ввод координат хода

        try:
            row, col = int(input('ВВедите номер строк: ')), int(input('Введите номер столбца: '))
        except ValueError:
            print('!!!!!!!!!!!!!!!!!!!')
            print('Нужно вводить число')
            print('!!!!!!!!!!!!!!!!!!!')
            continue

        # Проверки на провильность хода и на наличие в выбраной ячейке Х или О

        if not checkmove(size, row, col):
            continue
        if istaken(row, col):
            continue

        # Проставление хода и проверка на выигрышь

        plrmove(row, col)
        if iswin(player, plrtag, a, size):
            print('')
            print(f'Выиграл {player.upper()}')
            print('')
            if plrscale == 1:
                statistic.stat['Player 1']['Win'] += 1
                statistic.stat['Player 2']['Loose'] += 1
            elif plrscale == 2:
                statistic.stat['Player 2']['Win'] += 1
                statistic.stat['PLayer 1']['Loose'] += 1
            print('')
            print('')
            break

        # Выведения изменённого поля

        print('')
        showfield()
        print('')

        counter += 1

        if size == 3:
            if counter == 9:
                print('Закончились свободные ячейки. Ничья')
                print('''

                    ''')
                break
