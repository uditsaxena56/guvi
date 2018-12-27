def armstrong(n):
    s=0
    x=n
    while n!=0:
        s=s+(n%10)**3
        n=n//10
    if x==s:
        print("yes")
    else:
        print("no")

try:
    n=int(input())
    armstrong(n)
except ValueError:
    print("Invalid input")
