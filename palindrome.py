def palindrome(n):
    x=0
    s=n
    while n !=0:
        x=x*10+n%10
        n=n//10
    if s == x:
        print("yes")
    else:
        print("no")

try:
    n=int(input())
    palindrome(n)
except ValueError:
    print("Invalid input")
