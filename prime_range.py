from math import *

def prime_range(m,n):
    for i in range(m+1,n):
        c=0
        for j in range(2,int(sqrt(i))+1):
            if i%j==0:
                c+=1
        if c==0:
            print(i,end=" ")

try:
    m,n=map(int,input().split())
    prime_range(m,n)
except ValueError:
    print("Invalid input")
