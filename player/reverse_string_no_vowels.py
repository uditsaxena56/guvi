def reverse(s):
    li=['a','e','i','o','u']
    for i in range(len(s)-1,-1,-1):
        if s[i] in li:
            pass
        else:
            print(s[i],end="")

try:
    n=int(input())
    s=input()
    reverse(s)
except ValueError:
    print("Invalid input")
