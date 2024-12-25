#Python's built-in map() function to apply a function to every element of an object.
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
#converted all the letters in each name to uppercase.
names_uppercase = []

for name in names:
  names_uppercase.append(name.upper())

# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)

names_map = map(str.upper, names)
print([*(names_map)])
