num = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]

list_1 = []
list_2 = []

for i in num:
    print(i)
    list_1.append(i)
    for x in num:
        list_2.append(list_1)
    list_1 = []

print(list_1)
print(list_2)