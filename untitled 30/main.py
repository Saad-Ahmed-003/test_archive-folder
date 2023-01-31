list_1 = {
    "name": {0: "test", 1: "saad"},
    "email": {0: "test@mail.com", 1: "saadbinsajid03@gmail.com"},
    "year": {0: 1996, 1: 2023},
    "month": {0: 12, 1: 1},
    "day": {0: 1, 1: 31}
}

num = 0
list_3 = []
list_2 = []

for i in list_1:
    for y in list_1[i]:
        if y == num:
            list_3.append(list_1[i][y])
print(len(list_3))
print(list_3)
