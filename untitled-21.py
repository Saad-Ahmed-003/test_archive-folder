D_List = [ {"a" : 1}, {"b" : 2}, {"c" : 3}, {"d" : 4}, {"e" : 5}]

all_auctions = []

for i in D_List:
    for x in i:
        all_auctions.append(i[x])

highest_number = 0

print(all_auctions)

for i in all_auctions:
    if highest_number < i :
        highest_number = i

print(highest_number)

