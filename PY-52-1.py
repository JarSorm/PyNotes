def perimetr_S(a):
    print("Периметр квадрата равен", a * 4)

def square_S(a):
    print("Площадь квадрата равна", a ** 2)

def dimensions_Rect(a, b):
    if a == b:
        print("Снова квадрат!")
    print(f"Периметр равен {2 * (a + b)}", f"Площадь равна {a * b}", sep='\n')

def circumference(d):
    from math import pi
    print(f'Длина окружности равна {"%.2f" %(pi * d)}')

def dimensions_Cube(a):
    print(f"Объём куба равен {a ** 3}", f"Площадь поверхности куба равна {6 * a ** 2}", sep='\n')

def dimensions_Prl(a, b, c):
    print(f"Объём параллелепипеда равен {a * b * c}", f"Площадь поверхности параллелепипеда равна {2 * (a * b + b * c + a * c)}", sep='\n')

def dimensions_Crcl(R):
    from math import pi
    print(f"Длина окружности равна {'%.2f' %(2 * pi * R)}", f"Площадь круга равна {'%.2f' %(pi * R ** 2)}", sep='\n')

def average(a, b):
    print(f"Среднее арифметическое равно {(a + b) / 2}")

def geometric_mean(a, b):
    print(f"Среднее геометриччесское равно {(a * b) ** 0.5}")

def math_sqr(a, b):
    print(f"Сумма {a ** 2 + b ** 2}", "\n" f"Разность (a^2-b^2) {a ** 2 - b ** 2}", "\n"
    f"Разность (b^2-a^2) {b ** 2 - a ** 2}" if a != b else "", "\n" f"Произведение {a ** 2 * b ** 2}",
    "\n" f"Частное (a^2/b^2) {'%.2F' %(a ** 2 / b ** 2)}", "\n" f"Частное (b^2/a^2) {'%.2F' %(b ** 2 / a ** 2)}" if a != b else "")
#1
a = float(input("1.Введите длину стороны квадрата для расчета его периметра: "))
perimetr_S(a)
#2
a = float(input("2.Введите длину стороны квадрата для расчета его площади: "))
square_S(a)
#3
print("3.Введите длины сторон прямоугольника для расчета его периметра и площади:")
a, b = float(input("а: ")), float(input("b: "))
dimensions_Rect(a, b)
#4
d = float(input("4.Введите диаметр окружности для расчета ее длины: "))
circumference(d)
#5
a = float(input("5.Введите длину ребра куба для расчета его объема и площади поверхности: "))
dimensions_Cube(a)
#6
print("6.Введите длины рёбер прямоугольного параллелипипеда для расчета его объема и площади поверхности:")
a, b , c = float(input("a: ")), float(input("b: ")), float(input("c: "))
dimensions_Prl(a, b, c)
#7
R = float(input("7.Введите радиус круга для расчета длины его окружности и площади: "))
dimensions_Crcl(R)
#8
print("8.Введите два числа для расчета их среднего арифметического:")
a, b = float(input("a: ")), float(input("b: "))
average(a, b)
#9
print("9.Введите два неотрицательных числа для расчета их среднего геометрического:")
a, b = float(input("a: ")), float(input("b: "))
while a < 0 or b < 0:
    print("Для расчетов требуются неотрицательные числа!")
    a, b = float(input("a: ")), float(input("b: "))
geometric_mean(a, b)
#10
print("10.Введите два ненулевых числа для расчета суммы, разности, произведения и частного их квадратов:")
a, b = float(input("a: ")), float(input("b: "))
while a == 0 or b == 0:
    print("Для расчетов требуются ненулевые числа!")
    a, b = float(input("a: ")), float(input("b: "))
math_sqr(a, b)