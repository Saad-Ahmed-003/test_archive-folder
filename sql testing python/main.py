import sqlite3

# create database
conn = sqlite3.connect('teacher.db')

name = "afifa"
a = "a"
b = "b"
email = "saad@212"
num = "1234567890"

# create cursor
c = conn.cursor()

# create a table
c.execute("""CREATE TABLE IF NOT EXISTS customers(
    name text,
    username text,
    email text
    )""")

c.execute(f"SELECT rowid, * FROM customers WHERE name = '{name}'")
items1 = c.fetchall()
print(items1[0][2])


conn.commit()
# commit code
conn.close()


def reade_teachers():
    conn1 = sqlite3.connect('teacher.db')
    cur = conn1.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS customers(
        name text,
        user text,
        password text,
        address text,
        email text,
        phone_number text 
    )
    """)
    cur.execute("SELECT rowid, * FROM customers")
    data = cur.fetchall()
    list1 = [i[2] for i in data]
    list2 = data
    conn1.commit()
    conn1.close()
    all_list = (list1, list2)
    return all_list


passe = []
man = reade_teachers()
for i in man[1]:
    passe.append(i[3])

dictionary = {k: v for (k, v) in zip(man[0], passe)}

print(dictionary)

ad = dictionary["saad♥❤ahmed03"]
print(ad)

if "ahmed" in dictionary:
    print(dictionary["ahmed"])
