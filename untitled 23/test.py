a = 2.5
b = 3.5
c = {"a": 1, "b": 2, "c": 3}
d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
e = {"a": 1, "b": 2, "c": 3}

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
for i in c:
    if e[i] == c[i]:
        print(i)
