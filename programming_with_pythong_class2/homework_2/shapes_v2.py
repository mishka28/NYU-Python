#!/usr/bin/env python3
class Shape():
    pi = 3.14159
    """docstring for shape"""
    def __init__(self, side, radius, shape_type):
        return     
    def add_ally(self,shape_object):
        self.allies.append(shape_object)
        return self.allies
    def add_enemies(self,shape_object):
        self.enemies.append(shape_object)
        return self.enemies
    def update_edge_length(self, change):
        try:
            self.side = self.side + change
            return self.side
        except:
            self.radius = self.radius + change
            return self.radius

class Triangle(Shape):
    def __init__(self, side = 0):
        self.side = side
        self.shape_type = self.__class__.__name__
        self.allies = []
        self.enemies = []
    def area(self):
        return (3**0.5) / 4 * self.side**2 
    def perimeter(self):
        return self.side * 3
    def __str__(self):
        return("Role: aggressive and prone to violence")
        
class Square(Shape):
    def __init__(self, side = 0):
        self.side = side
        self.shape_type = self.__class__.__name__
        self.allies = []
        self.enemies = []
    def area(self):
        return self.side * self.side
    def __str__(self):
        print("Role: complacent and bureacratic")
    def perimeter(self):
        return self.side * 4

class Circle(Shape): 
    pi = 3.14159
    def __init__(self, radius = 0):
        self.radius = radius
        self.shape_type = self.__class__.__name__
        self.allies = []
        self.enemies = []
    def area(self):
        return self.radius**2 * self.__class__.pi
    def perimeter(self):
        return self.radius * 2 * self.__class__.pi
    def __str__(self):
        return("Role: wise and noble")

class Pentagon(Shape):
    def __init__(self, side = 0):
        self.side = side
        self.shape_type = self.__class__.__name__
        self.allies = []
        self.enemies = []
    def area(self):
        return 0.25 *((5*(5**0.5 * 2 +5))**0.5) * self.side**2 
    def perimeter(self):
        return self.side * 5
    def __str__(self):
        return("Role: Pentagon")

class Hexagon(Shape):
    def __init__(self, side = 0):
        self.side = side
        self.shape_type = self.__class__.__name__
        self.allies = []
        self.enemies = []
    def area(self):
        return 3 * 3**0.5 / 2 * self.side**2 
    def perimeter(self):
        return self.side * 6
    def __str__(self):
        return("Role: Hexagon")

class Star(Shape):
    def __init__(self, side = 0):
        self.side = side
        self.shape_type = self.__class__.__name__
        self.allies = []
        self.enemies = []
    def area(self):
        return "Complicated" 
    def perimeter(self):
        return self.side * 10
    def __str__(self):
        return("Role: Star")



if __name__ == "__main__":
    c_r = 1 #define radius for the circle
    s_s = 1 #define the side for the square
    t_s = 4 #define the side of the triangle
    c = Circle(c_r)
    s = Square(s_s) 
    t = Triangle(t_s)

    print("Choose a shape from a list below")
    print( "{} with radius = {}".format(c.shape_type , c_r))
    print( "{} with side = {}".format(s.shape_type , s_s))
    print( "{} with side = {}".format(t.shape_type , t_s))

    for retry in range(3): #3 tries to pick as shape
        choice = raw_input()
        if choice == "Circle":
            x = c #set x to class Circle
            break
        elif choice == "Triangle":
            x = t #set x to class Triangle
            break
        elif choice == "Square":
            x = s #set x to class Square
            break
        else:
            print("Has to be either of 3 with the CamelCase \n {} \n {} \n {} \nPlease try again".format(c.shape_type, s.shape_type, t.shape_type))
    else:
        print("You failed 3 times you Suck!")
        exit(1)        
    
    print("Do you want to know, area and perimeter of the {}? choose Yes or No".format(x.shape_type))
    y_n = raw_input()
    if y_n == "Yes": #Yes or No is they want to know area and parameter
        print("area = {} \nradius = {}".format(x.area() , x.perimeter()))
    elif y_n == "No":
        print("Why not? Anyways")
    else:
        print("Default \narea = {} \nradius = {}".format(x.area() , x.perimeter()))
    #List the enemies and allies and let the modify with anything they want
    print("Here is the list of {}`s friends and enemies".format(x.shape_type))
    print("friends = {} enemies = {}".format(x.allies , x.enemies))
    print("Add a friend for {}".format(x.shape_type))
    x.add_ally(raw_input())
    print("Add an enemy for {}".format(x.shape_type))
    x.add_enemies(raw_input())
    print("Here is the update list of {}'s friends and enemies".format(x.shape_type))
    print("friends {} with radius = {}".format(x.allies , x.enemies))
    print("What a fun but silly game, aren`t you happy it`s finally over?")


    # print(c.area())
    # c.update_edge_length(2)
    # print(c.area())
    # print(s.area())
    # s.update_edge_length(2)
    # print(s.area())

    # t.add_ally("Circle")
    # t.add_enemies("Square")
    # c.add_ally("Triangle")
    # c.add_enemies("Square")
    # s.add_enemies("Triangle")
    # s.add_enemies("Square")
    # print(t.shape_type)
    # print("friends:",t.allies)
    # print("enemies:",t.enemies)
    # print(c.shape_type)
    # print("friends:",c.allies)
    # print("enemies:",c.enemies)
    # print(s.shape_type)
    # print("friends:",s.allies)
    # print("enemies:",s.enemies)

    # t.add_ally("Circle")
    # t.add_enemies("Square")

    # print(t.shape_type)
    # print("friends:",t.allies)
    # print("enemies:",t.enemies)

