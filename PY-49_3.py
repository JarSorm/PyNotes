# 3
def average():
    counter = 0
    n = int(input('Введите следующее число: '))
    summ_n = n
    while n != 0:
        n = int(input('Введите следующее число: '))
        counter += 1
        summ_n += n
    return summ_n / counter


# 4
def num_raw():
    for i in range(0, 101):
        print(i, end=' ')


# 5
def multiplication_table():
    for i in range(0, 10):
        for j in range(1, 10):
            print(f'{i}*{j}={i * j}')


# 6
def print_list_dict():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    d = {'first': 1,
         'second': 2,
         'fird': 3,
         }
    for i in l:
        print(i)
    for j in d:
        print(j, d.get(j))


# print(average())
# num_raw()
# multiplication_table()
# print_list_dict()
