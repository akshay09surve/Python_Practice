point = (1,2)
nums = 3,4
print(type(nums))

combinedTuple = point+nums
print(combinedTuple)

# Accessing tuple elements
print(combinedTuple[0:3])

# Unpacking tuple
x,y,z,t = combinedTuple
print(x,t)

# Finding tuple elements
if 10 in combinedTuple:
    print("exists")

