try:
    m,n=map(int,input().split())
    for i in range(m+1,n):
        if i%2==0:
            print(i,end=" ")
except ValueError:
    print("Invalid input")
