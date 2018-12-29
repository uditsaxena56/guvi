def repeat(n,li):
    r=[]
    li.sort()
    for i in range(0,n):
        for j in range(i+1,n):
            if li[i]==li[j] and li[i] not in r:
                r.append(li[i])
    if len(r)==0:
        print("unique")
    else:
        for i in r:
            print(i,end=" ")

try:
    n=int(input())
    li=list(map(int,input().split()))
    repeat(n,li)
except ValueError:
    print("Invalid input")
