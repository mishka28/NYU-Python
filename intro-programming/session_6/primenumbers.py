#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    #increment = 1
    #the_range = range(a,b + increment)      
    
    for n in range(a, b):
        for x in range(a, n):
            if n % x == 0:              
                print(n, "equals", x, "*", n//x)
            break
        else:
            # loop fell through without finding a factor
            print(n, "is a prime number")

        







    #if ( a > b ):
    #   print("a > b")
    #elif ( a < b ):
    #   print("a < b")
    #else:
    #    print("a = b")

