n = int(input("number :- "))

mach = n % 1
mach2 = n % n

print(type(mach), type(mach2))

if mach == 0 and mach2 == 0:
    print("It's a prime number.")
else:
    print("It's not a prime number")

devided_numbers = []

for i in range(2, n):
    devided_numbers += str(n % i)
    print(devided_numbers)

if '0' in devided_numbers:
    print("It's not a prime number")
else:
    print("It's a prime number.")