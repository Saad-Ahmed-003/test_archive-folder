tata = True
data = 0
while data < 10:
    data += 1
    print(data)
    while data < 10:
        print(data)
        break
        print("un broken")
    print("broken")