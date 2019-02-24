#!/user/bin/env python3

def four():
    x = 0 
    while x < 4:
        print("in generator, x = ", x)
        yield x 
        x += 1

def infi():
    x = 0 
    while True:
        print("in generator, x = ", x)
        yield x 
        x += 1

def more():
    x = 0 
    while x < 4:
        print("in generator, x = ", x)
        yield x 
        x += 1

if __name__ == "__main__":
    for i in four():
        print(i)


