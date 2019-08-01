__author__ = 'Alex Nik'

#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random

def ran_number():
    return random.randint(0, 90)

def creat_str(*args):
    final_str = ['  ']
    for i in range(1, 10):
        final_str.append('  ')

    existing_nums = list(args)[0]
    str_card = []
    x = ran_number()
    for i in range(1, 6):
        while x in existing_nums:
            x = ran_number()
        for j in range(0, 10):
            existing_nums.append((x // 10) * 10 + j)
        str_card.append(x)

    for j in str_card:
        for i in range(0, 10):
            if i == j // 10:
                final_str[i] = j
    return final_str

def creat_card():
    existing_nums = []
    card = []
    for i in range(1, 4):
        existing_nums = []
        for j in card:
            for h in j:
                existing_nums.append(h)
        card.append(creat_str(existing_nums))
    return card

def printing(card):
    for i in card:
        if i[0] == '  ':
            print(' '.join(map(str, i)))
        else:
            print(' ' + ' '.join(map(str, i)))
    print('-----------------------------')
    return

def check_PC(num, card, pc_score):
    winner = 0
    for i in range(0, 3):
        for j in card[i]:
            if num == j:
                z = card[i].index(j)
                card[i][z] = 'xx'
                pc_score += 1
    if pc_score == 15:
        winner = 1
        print('Победаил РС\n')
    return  winner

def check(num, card, user_score, user_answer):
    answer = 'N'
    winner = 0
    for i in range(0, 3):
        for j in card[i]:
            if num == j:
                z = card[i].index(j)
                card[i][z] = 'xx'
                user_score += 1
                answer = 'Y'
    if answer.upper() != user_answer.upper():
        print('Вы ошиблись, победаил РС\n')
        winner = 1
    elif answer == 'Y':
        print('Выпал номер из карточки\n')
        if user_score == 15:
            print('Поздравляем! Вы победили!\n')
            winner = 1
    else:
        print('Вы правы, продолжаем игру!\n')
    return winner


user_card = creat_card()
pc_card = creat_card()

user_answer_check = ['Y', 'N']
user_answer = ''
user_score = 14
pc_score = 14
winner = 0
score = 90
num = ran_number()
existing_nums = []
while winner == 0 and score != 0 and pc_score != 15 and user_score != 15:
    while num in existing_nums:
        num = ran_number()
    existing_nums.append(num)
    score -= 1
    print(f'Новый бочонок: {num} (осталось {score})\n------- Ваша карточка -------')
    printing(user_card)
    print('---- Карточка компьютера ----')
    printing(pc_card)
    user_answer = input('Зачеркнуть цифру? (y/n)')
    winner = check(num, user_card, user_score, user_answer)
    if winner != 1:
        winner = check_PC(num, pc_card, pc_score)
