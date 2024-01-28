from sys import getsizeof

# Generator data structure to store objects
tup = (x*2 for x in range(10000))
# print(type(tup))
# for x in tup:
#     print(x)
print("Generator : ", getsizeof(tup))
# Generator data structure doesnt assign memory to the objects in it
# So, we can find out how many objects are stored in a generator
print(len(tup)) 

# To access the objects stored in a generator we have to iterate over the generator
