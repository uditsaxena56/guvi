def reverse_number(n):
    x=0
    while n!=0:
        x=x*10+n%10
        n=n//10
    print(x)

try:
    n=int(input())
    reverse_number(n)
except ValueError:
    print("Invalid Input")
