products = [
    ("P1",10),
    ("P2",8),
    ("P3",12),
    ("P4",5)
]

# Basic method to filter the list according to need
# filtered = []
# for pr in products:
#     if pr[1]<=8:
#         filtered.append(pr[0])
# print(filtered)

# Use of filter function
print(list(filter(lambda pr:pr[1]>7,products)))