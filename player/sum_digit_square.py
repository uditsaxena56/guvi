def sum_digit(n):
    s=0
    while n!=0:
        s=s+(n%10)**2
        n=n//10
    print(s)

try:
    n=int(input())
    sum_digit(n)
except ValueError:
    print("Invalid Input")
