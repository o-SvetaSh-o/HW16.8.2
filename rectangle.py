class Rectangle: #задаем класс Прямоугольник
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def get_area(self): #вычисляем площадь прямоугольника
        return self.a*self.b
class Square: #задаем класс Квадрат
        def __init__(self,a):
        self.a = a
    def get_area_square(self):#вычисляем площадь квадрата
        return self.a ** 2
class Circle:
    def __init__(self,r): #задаем класс Круг
        self.r=r
    def get_area_circle(self): #вычисляем площадь круга
        return self.r**2*3.141525