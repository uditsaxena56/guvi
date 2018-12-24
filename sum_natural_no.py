def natural_sum(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    print(s)

try:
    n=int(input())
    natural_sum(n)
except ValueError:
    print("Invalid Input")
