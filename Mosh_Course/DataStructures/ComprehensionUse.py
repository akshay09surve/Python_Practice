# We can use comprehensions on list, set, dictionary

# Comprehension expression to get list of numbers
values = [num*2 for num in range(5)]
print(values)

# Comprehension expression to get set of numbers
val2 = {num*2 for num in range(9)}
print(val2)

# Comprehension expression to get dictionary of numbers
val3 = {num:num*2 for num in range(5)}
print(val3)

# Comprehension expression to get tuple of numbers
tup = (num*2 for num in range(5))
print(tup)