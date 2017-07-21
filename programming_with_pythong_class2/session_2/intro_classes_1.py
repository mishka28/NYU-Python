#!/usr/bin/env python3 

import sys

class Circle:
    # class variable
    pi = 3.14159
    def __init__(self,radius = 1):
        # instance variables
        self.radius = radius
    # instance methods
    def area(self):
        return self.radius**2 * 3.14159

if __name__ == "__main__":
    r = int(sys.argv[1])
    my_circle = Circle(r)
    print(2 * Circle.pi * my_circle.radius)
    print(my_circle.area())

