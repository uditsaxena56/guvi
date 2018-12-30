def even_odd_places(n,li):
    for i in range(n):
        if i%2==0 and li[i]%2!=0:
            print(li[i],end=" ")
        if i%2!=0 and li[i]%2==0:
            print(li[i],end=" ")

try:
    n=int(input())
    li=list(map(int,input().split()))
    even_odd_places(n,li)
except ValueError:
    print("Invalid Input")
