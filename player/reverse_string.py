def reverse(s):
    for i in range(len(s)-1,-1,-1):
        print(s[i],end="")

try:
    s=input()
    reverse(s)
except ValueError:
    print("Invalid input")
