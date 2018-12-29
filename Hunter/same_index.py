def same_index(n,li):
    s=[]
    for i in range(n):
        if li[i]==i:
            s.append(li[i])
    if len(s)==0:
        print("-1")
    else:
        s.sort()
        for i in s:
            print(i,end=" ")

    
try:
    n=int(input())
    li=list(map(int,input().split()))
    same_index(n,li)
except ValueError:
    print("Invalid Input")
