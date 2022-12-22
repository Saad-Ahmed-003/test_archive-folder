import random
guess_the_number = random.choice(range(1,101))
data = 9
print(guess_the_number)

while data > 0:
    print(data)
    data1 = int(input("input"))
    if data1 < guess_the_number:
        print("to")
    elif data1 > guess_the_number:
        print("low")
    elif data1 == guess_the_number:
        print("yes")
    data -= 1

