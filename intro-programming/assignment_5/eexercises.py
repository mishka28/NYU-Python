#!/usr/bin/env python3

import sys
import pdb


# pdb.set_trace()

#deg_C = int(sys.argv[1])
#b = int(sys.argv[2])


def to_fahr(deg_c):
    deg_f =  deg_c*1.8 + 32
    return(deg_f)

def to_cels(deg_fa):
    deg_ce =  5/9*(deg_fa - 32)
    return(deg_ce)

def main():
    deg_c = int(sys.argv[1])
    deg_fa = int(sys.argv[2])
    print("F = " , to_fahr(deg_c))
    print("C = " , to_cels(deg_fa))
    

if __name__ == '__main__':
    main()














