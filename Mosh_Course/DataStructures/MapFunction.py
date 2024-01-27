products = [
    ("P1",10),
    ("P2",8),
    ("P3",12)
]

# Basic method
# prices = []
# for product in products:
#     prices.append(product[1])

# print(prices)


# Use of map function
items = list(map(lambda item:item[1],products))
print(sorted(items))