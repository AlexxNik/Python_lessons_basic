__author__ = 'Alex Nik'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

path = os.getcwd()
print(f'The current directory: {path}')
try:
    folders_count = int(input('Set the number of folders:'))
except ValueError:
    print('An integer is required')
else:
    for i in range(1, folders_count + 1):
        try:
            os.mkdir(f'{path}/dir_{i}')
        except OSError:
            print(f'The folders is not created')
        else:
            print(f'The folder {path}/dir_{i} is created successfully')

for dirs in os.listdir(path):
    subfolder = os.path.join(path, dirs)
    if os.path.isdir(subfolder):
        os.rmdir(subfolder)
        print(f'The empty folder {subfolder} is deleted')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
count = 0
for dirs in os.listdir(path):
    subfolder = os.path.join(path, dirs)
    if os.path.isdir(subfolder):
        print(f'The current folder contains {subfolder}')
        count += 1
if count == 0:
    print("The folders isn't in current directory")

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

from shutil import copy
from inspect import getsourcefile

def creat_file_copy(file_name):
    return copy(getsourcefile(lambda: 0), f'{file_name}.py')

name = input('Input new files name: ')
creat_file_copy(name)
print(f'The file {name} is created successfully')