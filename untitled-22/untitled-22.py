import art

print(art.logo)

art1 = {}
art2 = []
num = 0
T_f = True

def add_bid(Name, Bid):
    art1 [Bid] = Name

while T_f == True:
    name = input("name")
    bid = int(input("bid"))
    ask = input("another one? 'Y' or 'N' \n")
    ask = ask.capitalize()
    print(ask)
    add_bid(name, str(bid))
    print(art1)
    if ask == "N":
        T_f = False
    elif ask == "Y":
        T_f = True



for i in art1:
    art2.append(int(i))
    if num < int(i):
        num = i
        print(num)


print(art1[str(num)])
print(art1)

