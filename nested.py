fruits = ["Apple", "Orange", "Pawpaw"]
names = ["Ola", "Ade", "Ubaydah"]
colors = ["Red", "Blue", "Pink"]

items = [fruits, names, colors]

print(items[2])

# Nested list
print(items[0][1])

# Get the following
# -> Ade, Red, Pink, Pawpaw
print(items[1][1:])

# List methods

# Lists are orderable
# Lists can be modified

# adding to the list
fruits += ["Guava", "Banana"]
fruits.append("Date")  # can only add one item
fruits.extend(["Mango", "Cherry"])

print(fruits)
