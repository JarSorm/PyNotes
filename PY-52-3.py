def num_pos(A):
    print(f"Число A является положительным - {A > 0}")

def num_odd(A):
    print(f"Число A является нечетным - {A % 2 > 0}")

def num_even(A):
    print(f"Число A является четным - {A % 2 == 0}")

def num_A_B_1(A, B):
    print(f"Справедливы неравенства A > 2 и B ≤ 3 - {A > 2 and B <= 3}")

def num_A_B_2(A, B):
    print(f"Справедливы неравенства A ≥ 0 или B < −2 - {A >= 0 or B < -2}")

def num_A_B_C_1(A, B, C):
    print(f"Справедливо двойное неравенство A < B < C - {A < B < C}")

def num_A_B_C_2(A, B, C):
    print(f"Число B находится между числами A и C - {A < B < C}")

def num_A_B_odd_AND(A, B):
    print(f"Каждое из чисел A и B нечетное - {A % 2 > 0 and B % 2 > 0}")

def num_A_B_odd_OR(A, B):
    print(f"Хотя бы одно из чисел A и B нечетное - {A % 2 > 0 or B % 2 > 0}")

def num_A_B_odd_XOR(A, B):
    print(f"Ровно одно из чисел A и B нечетное - {bool(A % 2 > 0) != bool(B % 2 > 0)}")
#1
A = int(input("1.Введите целое число: "))
num_pos(A)
#2
A = int(input("2.Введите целое число: "))
num_odd(A)
#3
A = int(input("3.Введите целое число: "))
num_even(A)
#4
print("4.Введите два целых числа:")
A, B = int(input("A: ")), int(input("B: "))
num_A_B_1(A, B)
#5
print("5.Введите два целых числа:")
A, B = int(input("A: ")), int(input("B: "))
num_A_B_2(A, B)
#6
print("6.Введите три целых числа:")
A, B, C = int(input("A: ")), int(input("B: ")), int(input("C: "))
num_A_B_C_1(A, B, C)
#7
print("7.Введите три целых числа:")
A, B, C = int(input("A: ")), int(input("B: ")), int(input("C: "))
num_A_B_C_2(A, B, C)
#8
print("8.Введите два целых числа:")
A, B = int(input("A: ")), int(input("B: "))
num_A_B_odd_AND(A, B)
#9
print("9.Введите два целых числа:")
A, B = int(input("A: ")), int(input("B: "))
num_A_B_odd_OR(A, B)
#10
print("10.Введите два целых числа:")
A, B = int(input("A: ")), int(input("B: "))
num_A_B_odd_XOR(A, B)