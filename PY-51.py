# If-Else
# 1
def count_positive():
    count = 0
    if int(input("Введите первое число: ")) > 0:
        count += 1
    for i in range(2):
        if int(input("Введите слудующее число: ")) > 0:
            count +=1
    return f'Количество положительных чисел в исходном наборе: {count}'


# 2
def max_number():
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    if x > y:
        return x
    return y


# 3
def max_min_number():
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    if x > y:
        return x, y
    elif y > x:
        return y, x
    else:
        return 'x = y'


# 4
def min_number():
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    z = int(input("Введите третье число: "))
    if x < y:
        if z < x:
            return z
        return x
    if z < y:
        return z
    return y


# 5
def spot_location():
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    if x > 0:
        if y > 0:
            return 1
        return 4
    if y > 0:
        return 2
    return 3


# Switch Case (match-Case)
# 1
def assessment(K :int):
    match K:
        case 1:
            return 'Плохо'
        case 2:
            return 'Неудовлетворительно'
        case 3:
            return 'удовлетворительно'
        case 4:
            return 'Хорошо'
        case 5:
            return 'Отлично'
        case _:
            return 'Ошибка'


# 2
def day_in_month(n):
    match n:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            return 28
        case _:
            return "Ошибка"


# 3
def calendar():
    d = int(input('Введите день: '))
    m = int(input('Введите месяц: '))
    match m:
        case 2:
            if d < 28:
                d += 1
            else:
                d, m = 1, m + 1
        case 4 | 6 | 9 | 11:
            if d < 30:
                d += 1
            else:
                d, m = 1, m + 1
        case 1 | 3 | 5 | 7 | 8 | 10:
            if d < 31:
                d += 1
            else:
                d, m = 1, m + 1
        case 12:
            if d < 31:
                d += 1
            else:
                d = m = 1

    print(f'следующая дата: {d}, {m}')


# 4
def robot():
    N = int(input('Введите команду для робота: '))
    direction = ['север', 'восток', 'юг', 'запад']
    while -1 <= N <= 1:
        match N:
            case -1:
                direction.insert(0, direction.pop())
                print(f'робот повернул налево и теперь движется на {direction[0]}')
            case 1:
                direction.insert(3, direction.pop(0))
                print(f'робот повернул направо и теперь движется на {direction[0]}')
            case 0:
                print(f'робот продолжает движение на {direction[0]}')
            case _:
                print('ошибка ввода')
        N = int(input('Введите следующую команду для робота: '))
    print('Программа робота завершена')


# 5
def num_to_word():
    n = int(input('целое число в диапазоне 100–999'))
    i = ''
    i_i = n // 100
    i_j = (n // 10) % 10
    i_k = n % 10
    l_j = ['', '', "двадцать ", "тридцать ", "сорок ", "пятьдесят ", "шестьдесят ", "семьдесят ", "восемьдесят ",
           "девяносто "]
    l_k = ['', "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одинадцать",
           "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать",
           "девятнадцать"]
    if i_j < 2:
        j, k = 0, i_j*10 + i_k
    else:
        j, k = i_j, i_k
    match i_i:
        case 1:
            i = 'сто '
        case 2:
            i = 'двести '
        case 3:
            i = 'триста '
        case 4:
            i = 'четыреста '
        case 5:
            i = 'пятьсот '
        case 6:
            i = 'шестьсот '
        case 7:
            i = 'семьсот '
        case 8:
            i = 'восемьсот'
        case 9:
            i = 'девятьсот '
        case _:
            return 'ошибка'
    return f'{i}{l_j[j]}{l_k[k]}'


# 6
def calculator():
    x = int(input('введите первое число: '))
    y = int(input('введите второе число: '))
    z = input('введите символ операции: ')
    match z:
        case '*':
            return f'{x}*{y}={x * y}'
        case '/':
            return f'{x}/{y}={x / y}'
        case '+':
            return f'{x}+{y}={x + y}'
        case '-':
            return f'{x}-{y}={x - y}'
        case _:
            return 'Ошибка операции'

calendar()