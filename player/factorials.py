def factorial(n):
    if n >20:
        print("Size too big")
    else:
        s=1
        for i in range(1,n+1):
            s=s*i
        return s

try:
    n=int(input())
    s=factorial(n)
    print(s)
except ValueError:
    print("Invalid input")
