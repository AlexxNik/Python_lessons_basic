__author__ = 'Alex Nik'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    n = int(n)
    m = int(m)
    fibonacci_list = [1, 1]
    for i in range(3, m + 1):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return fibonacci_list[n - 1 : m]

user_N = 'f'
user_M = 'f'
while user_N.isalpha() or user_M.isalpha() or int(user_M) < 2:
    user_N = input('Введите номер начального элемента ряда Фибоначчи: ')
    user_M = input('Введите номер конечного элемента ряда Фибоначчи: ')
print(fibonacci(user_N, user_M))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    for i in range(len(origin_list)):
        for j in range(len(origin_list)-i-1):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
    return print(f'\nИсходный список: [2, 10, -12, 2.5, 20, -11, 4, 4, 0]\nСортировка завершена: {origin_list}')

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def func(positive):
    if positive > 0:
        return  1
    else:
        return  0

def my_filt(func, obj):
    result = []
    for i in obj:
        if func(i) == 1:
            result.append(i)
    return result

my_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
check = my_filt(func, my_list)
print(f'\nИсходный список: {my_list}\nОтфильтрованы положительные значения: {check}')

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def maxim(user_list):
    max = 0
    max_index = 0
    for i in user_list:
        if i > max:
            max = i
            max_index = user_list.index(i)
    return max_index

def minim(user_list):
    min = maxim(user_list)
    min_index = 0
    for i in user_list:
        if i < min:
            min = i
            min_index = user_list.index(i)
    return min_index

def parallelograms_check(A1, A2, A3, A4):
    x_center1 = 0
    y_center1 = 0
    x_center2 = 0
    y_center2 = 0
    par_set = list(zip(A1, A2, A3, A4))
    par_list_x = par_set[0]
    par_list_y = par_set[1]
    x_center1 = (par_list_x[maxim(par_list_x)] + par_list_x[minim(par_list_x)]) / 2
    y_center1 = (par_list_y[maxim(par_list_x)] + par_list_y[minim(par_list_x)]) / 2
    par_set2 = [A1, A2, A3, A4]
    par_set2.pop(maxim(par_list_x))
    par_set2.pop(minim(par_list_x))
    par_set2 = (list(par_set2[0]), list(par_set2[1]))
    par_set2 = list(zip(par_set2[0], par_set2[1]))
    par_list_x2 = par_set2[0]
    par_list_y2 = par_set2[1]
    x_center2 = (par_list_x2[0] + par_list_x2[1]) / 2
    y_center2 = (par_list_y2[0] + par_list_y2[1]) / 2
    if x_center1 == x_center2 and y_center1 == y_center2:
        return print(f'Данная фигура является параллелограммом с координатами вершин: {A1}, {A2}, {A3}, {A4}')
    else:
        return print(f'Данная фигура с координатами вершин: {A1}, {A2}, {A3}, {A4} - не параллелограмм')

A1 = [-14, 8]
A2 = [-3, 11]
A3 = [12, -4]
A4 = [1, -7]
parallelograms_check(A1, A2, A3, A4)

A1 = [-14, 9]
A2 = [-3, 11]
A3 = [12, -4]
A4 = [1, -7]
parallelograms_check(A1, A2, A3, A4)