def min_div(m,n):
    for i in range(max(m,n),(m*n)+1):
        if i%m==0 and i%n==0:
            print(i)
            break

try:
    m,n=map(int,input().split())
    min_div(m,n)
except ValueError:
    print("Invalid Input")
