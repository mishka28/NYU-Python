import sys

def to_celsius(degF):
    degC = 5/9*(degF - 32)
    return degC

def main():
    try:
        degF = float(sys.argv[1])
        print(to_celsius(degF))
    except: 
        print("input bumber as argument")
if __name__ == '__main__':
    main()
