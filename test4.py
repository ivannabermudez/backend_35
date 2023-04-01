
def print_total():
    print("your total is:123")


def can_drink(age):
    if age < 21:
        print("you can't drink")
    else:
        print("you may drink")

def users():
    people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35},
    {'name': 'Dave', 'age': 40},
    {'name': 'Emily', 'age': 45},
]

for user in people:
     print(user) 

print("2- only names") 
for user in people:
    print(user["name"])

print("3-users over 30")
for user in people:
    if (user ["age"] > 30):
        print (user["name"] + "-" + str(user["age"] ))

print("4 - total ages") 
total = 0
for user in people:
    total+= user["age"]

print(f"Total is: {total}") 
print("Total is: " + str(total))
      
print ("5 - find by name")
name = input("Type the user name: ")

found = False 
for user in people:
    if user["name"].lower() == name.lower():
        found = True
        print(f"{user['name']} => {user['age']}")

if not found:
    print("Error: User not found")




print_total()

can_drink(19) #no
can_drink(24) # yes
users()

