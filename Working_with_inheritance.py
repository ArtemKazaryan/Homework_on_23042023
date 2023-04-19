
# !!!!!!  ДЛЯ ЗАПУСКА ОТДЕЛЬНЫХ ЗАДАНИЙ РАСКОММЕНТИРУЙТЕ ИХ РЕШЕНИЕ, ЕСЛИ ПОТРЕБУЕТСЯ  !!!!!!

# Домашняя работа на 23.04.2023.

# Модуль 10. Объектно-ориентированное
# программирование
#
# Тема: Множественное наследование. Полиморфизм.
# Реализация магических методов. Часть 6

# Задание 1
# Создать базовый класс Фигура с методом для подсчета
# площади. Создать производные классы: прямоугольник,
# круг, прямоугольный треугольник, трапеция со своими
# методами для подсчета площади.
#
# Решение:
print()
print('-'*49)
print('*'*11, 'РЕЗУЛЬТАТЫ ПО ЗАДАНИЮ №1:', '*'*11)

from math import pi

class Figure:
    print()
    print(f'Площади известных фигур:')
    def get_area(self):
        pass

class Rectangle(Figure):
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2

    def get_area(self):
        print(f'Площадь прямоугольника со сторонами {self.side_1} и {self.side_2} равна {self.side_1 * self.side_2}')
        return self.side_1 * self.side_2

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        print(f'Площадь круга с радиусом {self.radius} равна {round(pi * self.radius ** 2, 3)}')
        return round(pi * self.radius ** 2, 3)

class RectangularTriangle(Figure):
    def __init__(self, cathet_1, cathet_2):
        self.cathet_1 = cathet_1
        self.cathet_2 = cathet_2

    def get_area(self):
        print(f'Площадь прямоугольного треугольника с катетами {self.cathet_1} и {self.cathet_2} равна {(self.cathet_1 * self.cathet_2) / 2}')
        return (self.cathet_1 * self.cathet_2) / 2

class Trapezoid(Figure):
    def __init__(self, basis_1, basis_2, height):
        self.basis_1 = basis_1
        self.basis_2 = basis_2
        self.height = height

    def get_area(self):
        print(f'Площадь трапеции с основаниями {self.basis_1} и {self.basis_2} и высотой {self.height} равна {self.height * (self.basis_1 + self.basis_2) / 2}')
        return self.height * (self.basis_1 + self.basis_2) / 2

print()
rectangle = Rectangle(5, 10)
circle = Circle(5.64)
rectangular_triangle = RectangularTriangle(3, 4)
trapezoid = Trapezoid(3, 4, 2)

rectangle.get_area()
circle.get_area()
rectangular_triangle.get_area()
trapezoid.get_area()





# Задание 2
# Для классов из задания 1 нужно переопределить магические методы int(возвращает площадь)
# и str(возвращает
# информацию о фигуре).
#
# Решение:



# Задание 3
# Создайте базовый класс Shape для рисования плоских
# фигур.
# Определите методы:
# ■ Show() — вывод на экран информации о фигуре;
# ■ Save() — сохранение фигуры в файл;
# ■ Load() — считывание фигуры из файла.
# Определите производные классы:
# ■ Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
# ■ Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
# ■ Circle — окружность с заданными координатами центра и радиусом;
# ■ Ellipse — эллипс с заданными координатами верхнего
# угла описанного вокруг него прямоугольника со сторонами, параллельными осям координат, и размерами
# этого прямоугольника.
# Создайте список фигур, сохраните фигуры в файл,
# загрузите в другой список и отобразите информацию о
# каждой из фигур.
#
# Решение:





