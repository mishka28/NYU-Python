#!/usr/bin/env python3

# import time_elaps

# print("hello world")
height = 10 

def get_fall_time(height):
    # gravity isn't going to change, units in m/(s^2)
    G = 9.8
    time_elapsed = ((2 * height) / G)**(0.5)

    # replace with logic of above equation
    return(time_elapsed)
    
    height = 10 

if __name__ == '__main__':

    print(get_fall_time(10))
