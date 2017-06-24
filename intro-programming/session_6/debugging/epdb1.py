# epdb1.py -- experiemnt with the Python debugger

import pdb

def combine(s1,s2):       # define subroutine combine, which...
    s3 = s1 + s2 + s1 
    s3 = '"' + s3 + '"'
    return s3



# pdb.set_trace()

if __name__ == '__main__':

    a = "aaa"
    b = "bbb"
    c = "ccc"

    final = combine(a,b)
    print(final)


