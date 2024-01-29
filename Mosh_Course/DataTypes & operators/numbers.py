import math

# Math module
print(round(2.8))
print(abs(-3.3))

print(math.ceil(2.1))

# Type conversion
# int(x), float(x), bool(x), str(x)
x = input("x : ")
y = int(x) + 1
print(f"x : {x}, y : {y}")

# Truthy and falsy values
# Falsy values - "", 0,
print(bool(""))
print(bool(" "))