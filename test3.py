colors = ['teal', 'PINK', 'PURPLE', 'ORANGE', 'green', 'BLUE', 'YELLOW', 'red', 'pink', 'TEaL', 'PurPLE', 'greEn', 'YELLOW', 'ORANnGE', 'blue', 'RED', 'teal', 'PINk', 'purPle', 'orange', 'GREEN', 'BluE', 'YelLow', 'ReD']

print(len(colors))

# case sensitive 

# create a list 

# travel the list of colors 

# get the color, parse it to lower, if the color is not in the list, append it 

results = []
for color in colors:
    color_lower = color.lower()
    if color_lower not in results:
        results.append(color_lower)

print(results)

# - given a color, count how many times it exists in the list 
#create a count equal to zero 
# travel the list of colors 
#if the color you are looking for is equal to the color from the list (in lowercase_
# #increase count by 1 (count = count + 1)
# print the result

color = "red"
count = 0
for c in colors:
    if color == c.lower():
        count = count =1

print(count)