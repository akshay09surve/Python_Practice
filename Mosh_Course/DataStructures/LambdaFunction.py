items = [
    ("P8",5),
    ("P6",3),
    ("P2",9)
]

# use of lambda expression
items.sort(key=lambda item:item[1])
print(items)