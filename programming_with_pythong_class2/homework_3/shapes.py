#!/usr/bin/env python3

class Triangle:
    def __init__(self, base = 0):
        self.base = base
        self.shape_type = "Triangle"
        self.allies = []
        self.enemies = []
    def area(self):
        return (3**0.5) / 4 * self.base**2 
    def perimeter(self):
        return self.base * 3
    def update_edge_length(self, change):
        self.base = self.base + change
        return self.base
    def add_ally(self,shape_object):
        self.allies.append(shape_object)
        return self.allies
    def add_enemies(self,shape_object):
        self.enemies.append(shape_object)
        return self.enemies
    def __str__(self):
        return("Role: aggressive and prone to violence")
        
class Square:
    def __init__(self, side = 0):
        self.side = side
        self.shape_type = "Square"
        self.allies = []
        self.enemies = []

    def area(self):
        return self.side * self.side
    def __str__(self):
        print("Role: complacent and bureacratic")
    def perimeter(self):
        return self.base * 4
    def update_edge_length(self, change):
        self.base = self.base + change
        return self.base
    def add_ally(self,shape_object):
        self.allies.append(shape_object)
        return self.allies
    def add_enemies(self,shape_object):
        self.enemies.append(shape_object)
        return self.enemies

class Circle:
    pi = 3.14159
    
    def __init__(self, radius = 0):
        self.radius = radius
        self.shape_type = "Circle"
        self.allies = []
        self.enemies = []
    def area(self):
        return self.radius**2 * self.__class__.pi
    def perimeter(self):
        return self.radius * 2 * self.__class__.pi
    def update_edge_length(self, change):
        self.base = self.base + change
        return self.base
    def add_ally(self,shape_object):
        self.allies.append(shape_object)
        return self.allies
    def add_enemies(self,shape_object):
        self.enemies.append(shape_object)
        return self.enemies
    def __str__(self):
        return("Role: wise and noble")

if __name__ == "__main__":
    t = Triangle(2 / (3**0.25))
    print(t.area())
    t = Triangle(4)
    print(t.area())
    print(type(t))
    c = Circle(1)
    s = Square(1)
    t.add_ally("Circle")
    t.add_enemies("Square")
    c.add_ally("Triangle")
    c.add_enemies("Square")
    s.add_enemies("Triangle")
    s.add_enemies("Square")
    print(t.shape_type)
    print("friends:",t.allies)
    print("enemies:",t.enemies)
    print(c.shape_type)
    print("friends:",c.allies)
    print("enemies:",c.enemies)
    print(s.shape_type)
    print("friends:",s.allies)
    print("enemies:",s.enemies)

