from math import *

def prime(n):
    c=0
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            c+=1
    if c==0:
        print("yes")
    else:
        print("no")

try:
    n=int(input())
    prime(n)
except ValueError:
    print("Invalid input")
