# Comprehension function/method is only used in python
# to achieve the tasks of map and filter functions

products = [
    ("P1",10),
    ("P2",8),
    ("P3",12),
    ("P4",5)
]

# Use of map function
# prices = list(map(lambda item:item[1],products))
# print(prices)

# # Use of filter function
# filtered_products = list(filter(lambda item:item[1]>7, products))
# print(filtered_products)

# Above things can be achieved with the help of comprehension 
pricelist = [item[1] for item in products] #Cleaner one line code
print(pricelist)

filtered = [item for item in products if item[1]>7]
filtered.sort(key=lambda item:item[1])
print(filtered)