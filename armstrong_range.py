def armstrong(m,n):
    for i in range(m+1,n):
        s=0
        x=i
        while i!=0:
            s=s+(i%10)**3
            i=i//10
        if x==s:
            print(x)

try:
    m,n=map(int,input().split())
    armstrong(m,n)
except ValueError:
    print("Invalid input")
