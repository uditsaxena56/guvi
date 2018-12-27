def multiples(n):
    for i in range(1,6):
        print(i*n,end=" ")

try:
    n=int(input())
    multiples(n)
except ValueError:
    print("Invalid input")
