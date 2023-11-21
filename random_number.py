import random
def game():
    my_num = int(random.randint(1, 10))
    print('Я загадал число. Угдай его')
    number = int(input('Введи число: '))
    while number != my_num:
        if number > my_num:
            print('Твое число больше загаданного')
        elif number < my_num:
            print('Твое число меньше загаданного')
        number = int(input('Введи число: '))
    print('Молодец! Ты угадал число!')

game()