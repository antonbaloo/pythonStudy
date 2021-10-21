a = int(input('ВВедите секунды: '))

hours = a // 3600
minutes = (a - (hours * 3600)) // 60
sec = a - (hours * 3600) - (minutes * 60)
print('{:02.0f}:{:02.0f}:{:02.0f}'.format(hours, minutes, sec))
