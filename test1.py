# import me in this file
from about import me

#print me to the console
print(me)

# go to the terminal and run test1 script
#"python3 test1,py"

# read data from the dict
print(me["name"])

#print the full name 
name = me["name"]
last = me ["last_name"]
print(name + " " + last)

#modify
me["preferred_color"] = "blue/gray"
print(me)

#
age = me["age"]
print(name + ": " + str(age))

# optional hw
#print the same ^ but using python string formatting 
# delete the age key from the dictionary and print the dictionary to confirm 

#string format- will obey everything that you type 
print(f"{name}: {age}")
print(f"   {age} - ., {name}")

#how to delete a key in dictionary 
del me["age"]