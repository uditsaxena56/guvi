def holiday(s):
    li=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if s in li:
        if s==li[0] or s==li[6]:
            print("yes")
        else:
            print("no")
    else:
        print("Invalid input")

s=input()
holiday(s)
