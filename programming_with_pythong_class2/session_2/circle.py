#!/usr/bin/env python3 

# circle module: contains the circle class.

class Circle:
    all_circles = []
    pi = 3.14159

    def __init__(self. r = 1):
        # Create a Circle with the given radius
        self.radius = r
        self.__class__.all_circles.append(self)
    
    def area(self):
        """ determine the area of the Circle"""
        return self.__class__.pi * self.radius**2
    
    @        
       
