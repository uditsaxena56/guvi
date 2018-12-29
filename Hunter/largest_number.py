def large(n,li):
    li.sort()
    s=0
    for i in range(n-1,-1,-1):
        s=s*10+li[i]
    print(s)

try:
    n=int(input())
    li=list(map(int,input().split()))
    large(n,li)
except ValueError:
    print("Invalid Input")
