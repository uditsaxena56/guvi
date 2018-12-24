def isleap(n):
    if n%4==0:
        if n%100==0:
            if n%400==0:
                print("yes")
            else:
                print("no")
        else:
            print("yes")
    else:
        print("no")

n=int(input())
isleap(n)
