#!/usr/bin/env python3

import sys
import math

def get_fall_time(height):
    # gravity isn't going to change, units in m/(s^2)
    G = 9.8
    time_elapsed = ((2 * height) / G)**(0.5)

    # replace with logic of above equation
    return(time_elapsed)

def main():
    height = float(sys.argv[1])
    print(get_fall_time(height))

if __name__ == '__main__':
    main()

