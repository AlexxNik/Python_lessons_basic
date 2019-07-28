
__author__ = 'AlexNik'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:
    def __init__(self, A, B, C):

        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)

        self.A = A
        self.B = B
        self.C = C
        self.AB = sideLen(self.A, self.B)
        self.BC = sideLen(self.B, self.C)
        self.CA = sideLen(self.C, self.A)

    def areaTriangle(self):
        semi_perimeter = self.perimeterTriangle() / 2

        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.AB)
                         * (semi_perimeter - self.BC)
                         * (semi_perimeter - self.CA))

    def perimeterTriangle(self):
        return self.AB + self.BC + self.CA

    def heightTriangle(self):
        return self.areaTriangle() / (self.AB / 2)


CheckTriang = Triangle((3, 2), (6, 7), (0, 12))
print(f'Площадь треугольника равна {CheckTriang.areaTriangle()}')
print(f'Высота треугольника равна {CheckTriang.heightTriangle()}')
print(f'Периметр треугольника равна {CheckTriang.perimeterTriangle()}')

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, A, B, C, D):

        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)

        def areaTriangle(len1, len2, len3):
            semi_perimeter = (len1 + len2 + len3) / 2

            return math.sqrt(semi_perimeter
                             * (semi_perimeter - len1)
                             * (semi_perimeter - len2)
                             * (semi_perimeter - len3))

        self.A = A
        self.B = B
        self.C = C
        self.D = D

        self.AB = sideLen(self.A, self.B)
        self.BC = sideLen(self.B, self.C)
        self.CD = sideLen(self.C, self.D)
        self.DA = sideLen(self.D, self.A)
        self.diagonal_AC = sideLen(self.C, self.A)
        self.diagonal_BD = sideLen(self.B, self.D)
        self.perimeter = self.AB + self.BC + self.CD + self.DA

        self.area = areaTriangle(self.AB, self.diagonal_BD, self.DA) \
                    + areaTriangle(self.diagonal_BD, self.BC, self.CD)

    def isTrapezeEqu(self):
        if self.diagonal_AC == self.diagonal_BD:
            return print('Фигура является равнобочной трапецией')
        return print('Фигура не является равнобочной трапецией')

    def Perimeter(self):
        print(f'Периметр трапеции: {self.perimeter}')

    def Area(self):
        print(f'Площадь трапеции: {self.area}')

    def sidesLen(self):
        print(f'Длинна сторон трапеции: {self.AB}, {self.BC}, {self.CD}, {self.DA}')

CheckTrapeze = Trapeze((-1, 3), (1, 3), (-6, 12), (6, 12))
CheckTrapeze.sidesLen()
CheckTrapeze.Area()
CheckTrapeze.Perimeter()
CheckTrapeze.isTrapezeEqu()
