class Car():
    def __init__(self, model, color, speed):
        self.model = "Ford"
        self.color = "red"
        self.speed = 0

    def accelerate(self, accels):
        self.speed += accels
        if (self.speed > 100):
            self.speed = 100
    
    def brake(self, braks):
        self.spped -= braks
        if (self.speed < 0):
            self.speed = 0
    
    def get_speed(self):
        return self.speed
    
class Animal():
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def speak(self):
        print(self.name + " is speaking")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name,age)
        self.name = name
        self.age = age

    def speak(self):
        print(self.name + "개 입니다.")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name,age)
        self.name = name
        self.age = age

    def speak(self):
        print(self.name + "고양이 입니다.")

class Shape():
    def get_area(self):
        pass
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def get_area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
