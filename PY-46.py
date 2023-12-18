from abc import ABC, abstractmethod


class StrAttr:
    """Дескриптор данных для атрибутов"""
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if 'wheels' in self.name:
            self.verify_int(value)
        setattr(instance, self.name, value)

    """Проверка типа данных для переменной wheels"""
    @classmethod
    def verify_int(cls, value):
        if not isinstance(value, int):
            raise ValueError('Введенные данные должны быть целым числом')


class MeansOfTransport:
    brand = StrAttr()
    color = StrAttr()
    wheels = StrAttr()

    def __init__(self, brand: str, color: str, wheels: int):
        self.brand = brand
        self.color = color
        self.wheels = wheels

    def show_color(self):
        print(self.color)

    def show_brand(self):
        print(self.brand)


class Car(MeansOfTransport):
    car_drive = 4

    def __init__(self, brand: str, color: str, wheels: int, year: int, price: int, amount: int):
        super().__init__(brand, color, wheels)
        self._year = year
        self.__price = price
        self.__amount = amount

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @classmethod
    def print_car_drive(cls):
        print(cls.car_drive)

    def __eq__(self, other):
        return self.__amount == other

    def __lt__(self, other):
        return self.__amount < other

    def __le__(self, other):
        return self.__amount <= other

    def __pos__(self):
        self.__amount += 1
        print('Завезли еще')

    def __neg__(self):
        if self.__amount >= 1:
            self.__amount -= 1
            print('Уехала')
        else:
            print('Кончились')

    def __abs__(self):
        self.__brand = 'Yamaha'
        self.__wheels = 2
        self.__year = 2023
        print('Все правильно сделал!')

    def __del__(self):
        print('End')


class Moped(MeansOfTransport):
    def __init__(self, brand: str, color: str, wheels: int):
        super().__init__(brand, color, wheels)

    @staticmethod
    def time(distance: float, max_speed: int):
        if isinstance(distance, float) and isinstance(max_speed, int) and max_speed > 0:
            time = distance / max_speed
            return time
        else:
            raise TypeError('Расстояние должно быть вещественным неотрицательным числом, '
                            'а скорость - целым положительным')


class Calculator:
    def __init__(self, a: (int, float)):
        self.__a = a

    def add(self, other: (int, float)):
        return self.__a + other


class StrngCalculator(Calculator):
    def __init__(self, a: str):
        super().__init__(a)

    def __add__(self, other: str):
        return self.add(other)


class Animals(ABC):

    @abstractmethod
    def voice(self):
        pass


class Cat(Animals):

    def voice(self):
        print('Кошка кричит "Мяу"')


class Dog(Animals):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Dog, cls).__new__(cls)
        return cls.instance

    def __init__(self, name, breed, color, age):
        self.__name = name
        self.__breed = breed
        self.__color = color
        self.__age = age

    def voice(self):
        print('Собака говорит "Гав"')

    def __str__(self):
        return f'{self.__name} + {self.__breed} + {self.__color} + {self.__age}'


a = MeansOfTransport('honda', "red", 4)
print(a.__dict__)