
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
# и str(возвращает информацию о фигуре).
#
# Решение:
print()
print('-'*49)
print('*'*11, 'РЕЗУЛЬТАТЫ ПО ЗАДАНИЮ №2:', '*'*11)

from math import pi

class Figure:
    print()
    print(f'Площади известных фигур:')
    def get_area(self):
        pass
    def __str__(self):
        return 'Это фигура!'
    def __int__(self):
        return self.get_area()

class Rectangle(Figure):
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2

    def get_area(self):
        print(f'int -> Площадь прямоугольника со сторонами {self.side_1} и {self.side_2} равна {self.side_1 * self.side_2}')
        return self.side_1 * self.side_2

    def __str__(self):
        return f'str -> Прямоугольник со сторонами {self.side_1} и {self.side_2}'

    def __int__(self):
        return int(self.get_area())

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        print(f'int -> Площадь круга с радиусом {self.radius} равна {round(pi * self.radius ** 2, 3)}')
        return round(pi * self.radius ** 2, 3)

    def __str__(self):
        return f'str -> Окружность с радиусом {self.radius}'

    def __int__(self):
        return int(self.get_area())

class RectangularTriangle(Figure):
    def __init__(self, cathet_1, cathet_2):
        self.cathet_1 = cathet_1
        self.cathet_2 = cathet_2

    def get_area(self):
        print(f'int -> Площадь прямоугольного треугольника с катетами {self.cathet_1} и {self.cathet_2} равна {(self.cathet_1 * self.cathet_2) / 2}')
        return (self.cathet_1 * self.cathet_2) / 2

    def __str__(self):
        return f'str -> Прямоугольный треугольник с катетами {self.cathet_1} и {self.cathet_2}'

    def __int__(self):
        return int(self.get_area())

class Trapezoid(Figure):
    def __init__(self, basis_1, basis_2, height):
        self.basis_1 = basis_1
        self.basis_2 = basis_2
        self.height = height

    def get_area(self):
        print(f'int -> Площадь трапеции с основаниями {self.basis_1} и {self.basis_2} и высотой {self.height} равна {self.height * (self.basis_1 + self.basis_2) / 2}')
        return self.height * (self.basis_1 + self.basis_2) / 2

    def __str__(self):
        return f'str -> Трапеция с основаниями {self.basis_1} и {self.basis_2} и высотой {self.height}'

    def __int__(self):
        return int(self.get_area())

print()
rectangle = Rectangle(5, 10)
print(str(rectangle))
int(rectangle)
print()
circle = Circle(5.64)
print(str(circle))
int(circle)
print()
rectangular_triangle = RectangularTriangle(3, 4)
print(str(rectangular_triangle))
int(rectangular_triangle)
print()
trapezoid = Trapezoid(3, 4, 2)
print(str(trapezoid))
int(trapezoid)



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
print()
print('-'*49)
print('*'*11, 'РЕЗУЛЬТАТЫ ПО ЗАДАНИЮ №3:', '*'*11)

# Создание родительского класса Shape(Фигуры):
class Shape:
    # В конструкторе родительского класса прописываем ввод координат левого верхнего угла фигуры,
    # конструктор в дальнейшем будет наследоваться с помощью функции super(), чтобы явно не ссылаться
    # на родительский класс, т.к. он на уровень выше для всех дочек:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Метод показа кооринат фигуры:
    def Show(self):
        print(f'Координаты: ({self.x},{self.y})')

    # Метод сохранения фигуры (её параметров, в данном случае координат левого верхнего угла) в файл:
    def Save(self, filename):
        with open(filename, 'w') as f:
            f.write(f'{self.x} {self.y}')

    # Метод загрузки из файла строки параметров фигуры:
    @staticmethod
    def Load(filename):
        with open(filename, 'r') as f:
            x, y = map(int, f.readline().split())
        return Shape(x, y)

# Создание дочернего класса Square(Квадрат) от родительского Shape(Фигуры):
class Square(Shape):
    # В конструкторе дочернего класса прописываем ввод координат левого верхнего угла квадрата и длину стороны
    # а аттрибуты экземпляра берём из суперкласса:
    def __init__(self, x, y, length):
        super().__init__(x, y)
        self.length = length

    # Метод показа кооринат квадрата:
    def Show(self):
        print(f'Квадрат: Координаты: ({self.x},{self.y}),'
              f' Длина: {self.length}')

    # Метод сохранения квадрата (его параметров) в файл:
    def Save(self, filename):
        with open(filename, 'w') as f:
            f.write(f'{self.x} {self.y} {self.length}')

    # Метод загрузки из файла строки параметров квадрата:
    @staticmethod
    def Load(filename):
        with open(filename, 'r') as f:
            x, y, length = map(int, f.readline().split())
        return Square(x, y, length)

# Создание дочернего класса Rectangle(Прямоугольник) от родительского Shape(Фигуры):
class Rectangle(Shape):
    # В конструкторе дочернего класса прописываем ввод координат левого верхнего угла прямоугольника,
    # ширину и высоту а аттрибуты экземпляра берём из суперкласса:
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    # Метод показа кооринат прямоугольника:
    def Show(self):
        print(f'Прямоугольник: Координаты: ({self.x},{self.y}),'
              f' Ширина: {self.width}, Высота: {self.height}')

    # Метод сохранения прямоугольника (его параметров) в файл:
    def Save(self, filename):
        with open(filename, 'w') as f:
            f.write(f'{self.x} {self.y} {self.width} {self.height}')

    # Метод загрузки из файла строки параметров прямоугольника:
    @staticmethod
    def Load(filename):
        with open(filename, 'r') as f:
            x, y, width, height = map(int, f.readline().split())
        return Rectangle(x, y, width, height)

# Создание дочернего класса Circle(Окружность) от родительского Shape(Фигуры):
class Circle(Shape):
    # В конструкторе дочернего класса прописываем ввод координат центра окружности и радиус
    # а аттрибуты экземпляра берём из суперкласса:
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    # Метод показа кооринат окружности:
    def Show(self):
        print(f'Круг: Координаты: ({self.x},{self.y}),'
              f' Радиус: {self.radius}')

    # Метод сохранения окружности (её параметров) в файл:
    def Save(self, filename):
        with open(filename, 'w') as f:
            f.write(f'{self.x} {self.y} {self.radius}')

    # Метод загрузки из файла строки параметров окружности:
    @staticmethod
    def Load(filename):
        with open(filename, 'r') as f:
            x, y, radius = map(int, f.readline().split())
        return Circle(x, y, radius)

# Создание дочернего класса Ellipse(Эллипс) от родительского Shape(Фигуры):
class Ellipse(Shape):
    # В конструкторе дочернего класса прописываем ввод координат (эллипса), а именно верхнего
    # угла описанного вокруг него прямоугольника со сторонами, параллельными осям координат, ширину и высоту
    # а аттрибуты экземпляра берём из суперкласса:
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    # Метод показа кооринат эллипса:
    def Show(self):
        print(f'Эллипс: Координаты: ({self.x},{self.y}),'
              f' Ширина: {self.width}, Высота: {self.height}')

    # Метод сохранения эллипса (его параметров) в файл:
    def Save(self, filename):
        with open(filename, 'w') as f:
            f.write(f'{self.x} {self.y} {self.width} {self.height}')

    # Метод загрузки из файла строки параметров эллипса:
    @staticmethod
    def Load(filename):
        with open(filename, 'r') as f:
            x, y, width, height = map(int, f.readline().split())
        return Ellipse(x, y, width, height)

print()
# Создание (прямо в списке) фигур с заданными параметрами как элементов списка shapes:
shapes = [Square(0, 0, 5), Rectangle(10, 10, 6, 4), Circle(20, 20, 3), Ellipse(30, 30, 8, 5)]

# Итерирование по списку
for shape in shapes:
    # Сохранение фигур в файлы с соответствующими названиями по ходу итерации
    shape.Save(f'{type(shape).__name__}.txt')
    # Загрузка фигур из файлов с соответствующими названиями по ходу итерации
    # в переменную new_shape классового типа
    new_shape = type(shape).Load(f'{type(shape).__name__}.txt')
    new_shape.Show()

