def only_once(n,li):
    li.sort()
    j=0
    while j < n:
        if j==n-1:
            print(li[j])
            j+=1
        elif li[j]==li[j+1]:
            j=j+2
        else:
            print(li[j])
            j+=1
            break
        

try:
    n=int(input())
    li=list(map(int,input().split()))
    only_once(n,li)
except ValueError:
    print("Invalid Input")
