__author__ = 'Alex Nik'

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import re
import copy

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
Result_1 = re.findall(r'[a-z]+', line)
if len(Result_1) != 1:
    print(Result_1)
else:
    print('Найден единственный диапазон значений в нижнем регистре')

print('\nАльтернативное решение без re:')
def LenList():
    return [new_line[SeparatePoint[i - 1] + 1: SeparatePoint[i]] for i in range(1, len(SeparatePoint)) if SeparatePoint[i] - 1 != SeparatePoint[i - 1]]

new_line = copy.deepcopy(line) #just try
SeparatePoint = [i for i in range(0, len(new_line)) if new_line[i].isupper()]
if len(SeparatePoint) == len(new_line):
    print('Нет значений в нижнем регистре\n\n')
else:
    if SeparatePoint[0] != 0:
        SeparatePoint.insert(0, -1)
    if new_line[-1].islower():
        SeparatePoint.append(len(new_line))
    Results = LenList()
    if len(Results) == 1:
        print('Нет значений в нижнем регистре, обрамляющих значения в верхнем регистре\n\n')
    else:
        print(f'{Results}\n\n')

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'
#line_2 = "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
Result_2 = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line_2)
print(Result_2)

print('\nАльтернативное решение без re:')
new_line2 = "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEec"
SeparatePointLeft = [i for i in range(2, len(new_line2) - 2) if new_line2[i - 2].islower() and new_line2[i - 1].islower()]
SeparatePointRight = [i for i in range(2, len(new_line2) - 2) if new_line2[i + 2].isupper() and new_line2[i + 1].isupper()]
Results_2 = [new_line2[SeparatePointLeft[i - 1] : SeparatePointRight[j]] for i in range(1, len(SeparatePointLeft)) for j in range(1, len(SeparatePointRight))]
print(Result_2)
# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import random

maximum_len = 0
num_repeat = 0
number = 0
RandomList = [random.randint(0, 9) for i in range(1, 2499)]
RandomList.insert(0, random.randint(1, 9))
try:
    Lesson_4 = open('Lesson_4.txt', 'w')
    for i in RandomList:
        Lesson_4.write(str(i))
except:
    Lesson_4.close()
with open('Lesson_4.txt') as Lesson_4:
    file_contents = Lesson_4.read()
    print(f'\nСодержание файла: {file_contents}')
num_repeat = re.findall(r'[^0]([0]+)[^0]', file_contents) + \
             re.findall(r'[^1]([1]+)[^1]', file_contents) + \
             re.findall(r'[^2]([2]+)[^2]', file_contents) + \
             re.findall(r'[^3]([3]+)[^3]', file_contents) + \
             re.findall(r'[^4]([4]+)[^4]', file_contents) + \
             re.findall(r'[^5]([5]+)[^5]', file_contents) + \
             re.findall(r'[^6]([6]+)[^6]', file_contents) + \
             re.findall(r'[^7]([7]+)[^7]', file_contents) + \
             re.findall(r'[^8]([8]+)[^8]', file_contents) + \
             re.findall(r'[^9]([9]+)[^9]', file_contents)
print(num_repeat)
for j in num_repeat:
    if maximum_len < len(j):
        maximum_len = len(j)
        number = j[0]
print(f'Максимальное количество повторений цифры {number} составляет {maximum_len}')