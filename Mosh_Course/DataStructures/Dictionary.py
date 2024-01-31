# Two ways todeclare a dictionary
point = {"x":1, "y":2} 
point = dict(x=1,y=2)
point["x"]=10
point["z"]=20
point["m"] = 13
# if "a" in point:
#     print(point["a"])

# # We get the tuple in each iteration using this method
# for key in point.items():
#     print(key)


# print(point.get("m",None))

# print(len(point))
# print(point["x"])

point.__iter__
try:
    point.__delitem__("m")
except KeyError:
    print("Value not found")
else:
    print("Object deleted")
print(point)
