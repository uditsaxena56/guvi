def power(n,p):
    s=1
    for i in range(p):
        s=s*n
    print(s)

try:
    n,p=map(int,input().split())
    power(n,p)
except ValueError:
    print("Invalid input")
