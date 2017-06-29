#!/usr/bin/env python3

import sys
import pdb


# pdb.set_trace()

#if __name__ == '__main__':
degrees_celsius = int(sys.argv[1])
b = int(sys.argv[2])


def to_fahrenheit(degrees_celsius):
    degrees_fahrenheit =  degrees_celsius*1.8 + 32
#        return degrees_fahrenheit
    print(degrees_fahrenheit)
