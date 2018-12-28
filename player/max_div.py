def max_div(m,n):
    for i in range(min(m,n),0,-1):
        if m%i==0 and n%i==0:
            print(i)
            break

try:
    m,n=map(int,input().split())
    max_div(m,n)
except ValueError:
    print("Invalid Input")
