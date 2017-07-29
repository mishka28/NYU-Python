#!/usr/bin/env python3
class shape:
    """docstring for shape"""
    def __init__(self, side, radius):
        self.side = side
        self.radius = radius
#        self.allies = []
#       self.enemies = []        
    def add_ally(self,shape_object):
        self.allies.append(shape_object)
        return self.allies
    def add_enemies(self,shape_object):
        self.enemies.append(shape_object)
        return self.enemies

class triangle(shape):
    def __init__(self, side = 0):
        self.side = side
        self.shape_type = "triangle"
        self.allies = []
        self.enemies = []
    def area(self):
        return (3**0.5) / 4 * self.side**2 
    def perimeter(self):
        return self.side * 3
    def update_edge_length(self, change):
        self.side = self.side + change
        return self.side
    def __str__(self):
        return("Role: aggressive and prone to violence")
        
class square:
    def __init__(self, side = 0):
        self.side = side
        self.shape_type = "square"
        self.allies = []
        self.enemies = []

    def area(self):
        return self.side * self.side
    def __str__(self):
        print("Role: complacent and bureacratic")
    def perimeter(self):
        return self.side * 4
    def update_edge_length(self, change):
        self.side = self.side + change
        return self.side
    def add_ally(self,shape_object):
        self.allies.append(shape_object)
        return self.allies
    def add_enemies(self,shape_object):
        self.enemies.append(shape_object)
        return self.enemies

class circle:
    pi = 3.14159
    
    def __init__(self, radius = 0):
        self.radius = radius
        self.shape_type = "circle"
        self.allies = []
        self.enemies = []
    def area(self):
        return self.radius**2 * self.__class__.pi
    def perimeter(self):
        return self.radius * 2 * self.__class__.pi
    def update_edge_length(self, change):
        self.side = self.side + change
        return self.side
    def add_ally(self,shape_object):
        self.allies.append(shape_object)
        return self.allies
    def add_enemies(self,shape_object):
        self.enemies.append(shape_object)
        return self.enemies
    def __str__(self):
        return("Role: wise and noble")

if __name__ == "__main__":
    t = triangle(4)
    print(str(t))

    t.add_ally("circle")
    t.add_enemies("square")

    print(t.shape_type)
    print("friends:",t.allies)
    print("enemies:",t.enemies)

