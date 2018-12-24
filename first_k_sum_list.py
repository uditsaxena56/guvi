n,k=map(int,input().split())
if k > n:
    print("k can not be greater than n")
else:
    s=0
    li=list(map(int,input().split()))
    for i in range(0,k):
        s=s+li[i]
    print(s)
