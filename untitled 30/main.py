list_1 = {
    "name": {0: "test", 1: "saad"},
    "email": {0: "test@mail.com", 1: "saadbinsajid03@gmail.com"},
    "year": {0: 1996, 1: 2023},
    "month": {0: 12, 1: 1},
    "day": {0: 1, 1: 31}
}

list_3 = []
list_2 = []


for i in list_1:
    for x in list_1[i]:
        if x == 0:
            list_3.append(list_1[i][x])
        elif x == 1:
            list_2.append(list_1[i][x])

print(list_3)
print(list_2)

