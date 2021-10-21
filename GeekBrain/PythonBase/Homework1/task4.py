a = int(input('num: '))
b = a % 10
a //= 10
while a > 0:
    if a%10 > b:
        b = a%10
    a //= 10
print(b)