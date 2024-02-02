#!/bin/python3
def isWeird(n):
    if (n%2 != 0): 
        print("Weird")
    elif (2<=n<=5):
        print("Not Weird")
    elif (6<=n<=20):
        print("Weird")
    else:
        print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    isWeird(n)
    
