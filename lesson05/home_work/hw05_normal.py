__author__ = 'Alex Nik'

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys
import shutil

def print_help():
    print('help - Getting help\n'
          'open_dir - Go to folder\n'
          'show_dirs_content - View the contents of the current folder\n'
          'del_dir - Remote folder\n'
          'make_dir - Create folder\n')
    return

def open_dir():
    try:
        user_dir = input('Enter the path to the folder:')
        os.chdir(f'{user_dir}')
    except OSError:
        return print(f'The folders is not found\n')
    else:
        return print(f'The folder {user_dir} is active\n')

def show_dirs_content():
    path = os.getcwd()
    print(f'The current directory: {path}')
    count = 0
    for dirs in os.listdir(path):
        subfolder = os.path.join(path, dirs)
        if os.path.isdir(subfolder):
            print(f'The current folder contains {subfolder}')
            count += 1
    if count == 0:
        print("There aren't folders in current directory\n")
    return

def del_dir():
    path = os.getcwd()
    print(f'The current directory: {path}')

    try:
        os.rmdir(path)
    except PermissionError:
        print(f'The empty folder {path} is not deleted') #не смог побороть эту ошибку...
    else:
        os.rmdir(path)
        print(f'The empty folder {path} is deleted\n')

def make_dir():
    path = os.getcwd()
    print(f'The current directory: {path}')
    try:
        user_dir = input('Enter the path to the new dir:')
        if user_dir == '':
            user_dir = path
        os.mkdir(user_dir)
    except OSError:
        print(f'The folders is not created')
    else:
        print(f'The folder {user_dir} is created successfully')
    return

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("ERROR: wrong key")
        print("Enter key help for support")

#Lesson_5
do = {'print_help': print_help(),
      'open_dir': open_dir(),
      'show_dirs_content': show_dirs_content(),
      'del_dir': del_dir(),
      'make_dir': make_dir()}