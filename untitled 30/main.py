list_1 = {
    "name": {0: "test", 1: "saad"},
    "email": {0: "test@mail.com", 1: "saadbinsajid03@gmail.com"},
    "year": {0: 1996, 1: 2023},
    "month": {0: 12, 1: 1},
    "day": {0: 1, 1: 31}
}

tuple_1 = ()
tuple_2 = ()


for i in list_1:
    for x in list_1[i]:
        if x == 0:
            tuple_1 += list_1[i][x]
        elif x == 1:
            tuple_2 += list_1[i][x]

print(tuple_1)
print(tuple_2)

