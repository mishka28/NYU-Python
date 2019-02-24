#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    increment = 1
    the_range = range(a,b + increment)      
    
    for i in the_range:
        print("a = " + str(i))
        







    #if ( a > b ):
    #   print("a > b")
    #elif ( a < b ):
    #   print("a < b")
    #else:
    #    print("a = b")

