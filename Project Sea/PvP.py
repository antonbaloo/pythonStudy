
from main import size as s
size = s
print('~~~~~~~~~~~~~')
print('Поле игрока 1')
print('')
a = []
for i in range(s):
    a.append([[0]] * s)
for i in a:
    print(i)

print('Игрок 1 размещает корабли')
print('Разместите 1 четырёхпалубный корабль')
for i in range(4):
    a[int(input('горизонталь'))][int(input('вертикаль'))] = [4]
print('')
print('Разместите 2 трёхпалубных корабля')
for i in range(2):
    for j in range(3):
        a[int(input('горизонталь'))][int(input('вертикаль'))] = [3]
print('')
for i in a:
    print(i, sep=' ')

size = s
print('~~~~~~~~~~~~~')
print('Поле игрока 2')
print('')
b = []
for i in range(s):
    b.append([[]] * s)
for i in b:
    print(i)
