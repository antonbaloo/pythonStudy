# Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

earnings = int(input('ВВедите сумму выручки: '))
cost = int(input('ВВедите сумму издержек: '))

if earnings > cost:
    print('Фирма прибыльная.')
    profit = earnings - cost
    print('Рентабельность: {:.1f}%'.format(profit/earnings*100))
    workers_amount = int(input('ВВедите количетво работников: '))
    print('Доход на 1 работника: {:.1f}'.format(profit / workers_amount))
elif cost > earnings:
    print('Форма убыточна.')
else:
    print('Фирма работает в ноль')