__author__ = 'Alex Nik'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    if float(number) == 0:
        return 'Округление невозможно: ' + number
    check = str(number)[0 : (len(str(int(float(number) // 1))) + int(ndigits) + 2)]
    if len(check[check.index('.') + 1 : ]) <= int(ndigits):
        return 'Округление не требуется: ' + check
    elif int(check[-1]) <= 4:
        return float(check[0 : -1])
    else:
        if check[-2] == '.':
            return float(check[0: -1]) + (1 / 10 ** int(ndigits))
        elif int(check[-2]) == 9 and float(check) >= 0:
            return float(check[0: -1]) + (1 / 10 ** int(ndigits))
        elif int(check[-2]) == 9 and float(check) < 0:
            return float(check[0: -1]) - (1 / 10 ** int(ndigits))
        else:
            return float(check[0 : -2] + str(int(check[-2]) + 1))

number = ''
ndigits = 0
while number.isalpha() or int(ndigits) <= 0:
    number = input('Введите число для округления: ')
    ndigits = input('Введите желаемое количество знаков после запятой')
    print('Введено неверное значение')
print(my_round(number, ndigits))
print(my_round(22.1234567, 5))
print(my_round(-2.1999947, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) == 6:
        left_numbers = list(str(ticket_number)[0 : 3])
        right_numbers = list(str(ticket_number)[3 : ])
        if sum(int (i) for i in left_numbers) == sum(int (i) for i in right_numbers):
            return 'Счастливый билет!'
        else:
            return 'Обычный билет...'
# ____another option____
#        left_numbers = 0
#        right_numbers = 0
#        for i in str(ticket_number)[0 : 3]:
#            left_numbers = left_numbers + int(i)
#        for i in str(ticket_number)[3 : ]:
#            right_numbers = right_numbers + int(i)
#        if left_numbers == right_numbers:
#            return 'Счастливый билет!'
#        else:
#            return 'Обычный билет...'
    else:
        return 'Данная программа проверяет только шестизначные номера билетов'

user_ticket = input('\n\nВведите шестизначный номер билета: ')
print(lucky_ticket(user_ticket))
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
