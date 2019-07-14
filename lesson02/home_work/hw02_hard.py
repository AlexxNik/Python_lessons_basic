__author__ = 'Alex Nik'

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
y = float(equation[(equation.index('=') + 2):equation.index('x')]) * x + float(equation[(equation.index('+') + 2):])
print(y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '14.07.2019'

month = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31,
         '09': 30, '10': 31, '11': 30, '12': 31}
if date.index('.') == 2 and date.index('.', 4) == 5 and len(date) == 10:
    if int(date[3:5]) >= 1 and int(date[3:5]) <=12:
        if int(date[0:2]) >= 1 and int(date[0:2]) <=31 and int(date[0:2]) <= month[date[3:5]]:
            if int(date[6:]) >= 1 and int(date[6:]) <= 9999:
                print('Дата введена корректно')
            else:
                print('Ошибка! Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999')
        else:
            print('Ошибка! День должен приводиться к целому числу в диапазоне от 1 до 30(31)')
    else:
        print('Ошибка! Месяц должен приводиться к целому числу в диапазоне от 1 до 12')
else:
    print('Ошибка! Длина исходной строки для частей должна быть в соответствии с форматом')


# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

room = int(input('Введите номер комнаты: '))
floor = 1
room_num = 1
same_floor = 2
if room == 1:
    print(1, 1)
else:
    while room_num < room:
        for i in range(1, same_floor + 1):
            room_num = room_num + same_floor
            floor += 1
            print('i', i)
            print('same_floor', same_floor)
            print('floor', floor)
            print('room_num', room_num)
            if room_num < room:
                i += 1
            else:
                break
        same_floor += 1

    if room == room_num:
        print(floor, same_floor - 1)
    else:
        print(floor, same_floor - 1 - (room_num - room))