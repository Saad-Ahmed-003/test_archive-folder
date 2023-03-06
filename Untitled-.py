list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

dictionary = {}

for i in range(len(list1)):
    print(i)
    dictionary[i] = {"name": list2[i], "time": list1[i]}

print(dictionary)
