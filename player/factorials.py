def factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    print(s)

try:
    n=int(input())
    factorial(n)
except ValueError:
    print("Invalid input")
