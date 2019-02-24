#!/usr/bin/env python3

import sys
import math
import time_elaps

tower_height = 2
tower_x = 0
tower_y = 0
target_x = 400
target_y = 300

def isVulnerable(tower_height, tower_x, tower_y, target_x, target_y):
    muzzle_velocity = 300

    # update this line to calculate time_in_air using get_fall_time() function
    time_in_air = time_elaps.get_fall_time(tower_height)

    tower_range = time_in_air * muzzle_velocity
    
    delta_x = tower_x - target_x  # difference between tower_x and target_x
    delta_y = tower_y - target_y  # difference between tower_y and target_y

    separation = ((delta_x ** 2) + (delta_y ** 2) ** (0.5))  # the x and y deltas form a triangle, find the hypotenuse
    
    if separation < tower_range:
        print("The target is closer than the tower range, what should we return?")
        return("TRUE")
    else:
        print("The target is further than the tower range, what should we return?")
        return("FALSE")

if __name__ == '__main__':
    print(isVulnerable(tower_height, tower_x, tower_y, target_x, target_y))
