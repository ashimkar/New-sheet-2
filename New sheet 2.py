import time

capitals = {"bangladesh": "dhaka",
             "india": "new delhi",
             "china": "bejing",
             "usa": "washington DC"}
capitals.update({"germany": "berlin"})

for key, value in capitals.items():
    print(key,value)

#print(capitals.get("china"))
#print(capitals.get("russia"))
#print(capitals.keys())
#print(capitals.values())

name = "ashim Kar"
if (name[0].islower()):
    name = name.capitalize()
print(name)
first_name = name[0:5].upper()
print(first_name)
last_name = name[6:9].lower()
print(last_name)
last_character = name[-1]
print(last_character)

student = ("ash", 26, "boy")
print (student.count("ash"))
print (student.index("boy"))
for x in student:
    print(x)
if "ash" in student:
    print("ash is a good boy")

grocery = {"egg", "bread", "sauce", "bowl"}
dishes = {"cup", "plate", "bowl"}
#grocery.add("napkin")
#grocery.update(dishes)
#dinner_table = grocery.union(dishes)
dinner_table = dishes.difference(grocery)
dinner_table = dishes.intersection(grocery)

for x in dinner_table:
    print(x)
#for x in grocery:
    print(x)

name = ""
while len(name) == 0:
    name = input("enter your name:")
print("hello"+name)

for i in range (10):
    print(i)
for i in range (10):
    print(i+1)

for i in range (50,100+1):
    print(i)

for i in range(50,100+1,2):
    print(i)
for i in "ashim":
    print(i)

for seconds in range (10,0,-1):
    print(seconds)
    time.sleep(1)
print("happy new year")

rows = int(input("how many rows are: "))
columns = int(input("how many columns are: "))
symbol = input("enter a symbol to use: ")

for i in range (rows):
    for j in range (columns):
        print(symbol, end="")
    print()
