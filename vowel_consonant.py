def isvowel(n):
    a="aeiou"
    if "a"<=n<="z" or "A"<=n<="Z":
        if n.lower() in a:
            print("Vowel")
        else:
            print("Consonant")
    else:
        print("Invalid")

n=input()
isvowel(n)
