values = list(range(5))
print(*values) # * is a spread operator

# Spread (*) operator to combine lists
first = [0,1,2]
second = "Hello"
comb = [*first,*second,"world"]
print(*comb)

# Spread (*) operator on dictionaries
# When combining 2 dictionaries, if any dictionaries have same key assigned to diff. values, last one taken is assigned
one = {"x":1}
two = {"x":10,"y":20}
combined = {**one,**two,"z":30}
print(combined)