a = 2.5
b = 3.5

if a < b:
    print("WTF")

a = a*100
a = int(a)

b = b*100
b = int(b)

if a < b:
    print("it worked")
elif b < a:
    print("this works")