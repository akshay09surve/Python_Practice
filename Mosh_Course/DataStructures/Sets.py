# Set is an unordered collection of unique items 
# and can not have any duplicate values

numbers = [1,3,2,1,4,4,5]

first = set(numbers)
second = {1,3}

# Combination of two sets - All unique elements
print(first | second)

# Intersection of two sets - common elements
print(first and second)

# Uncommon elements
print(first-second)

# 
print(first ^ second)
