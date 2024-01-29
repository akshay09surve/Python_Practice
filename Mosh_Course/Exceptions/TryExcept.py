try:
    # With statement is used with certain type of datatypes
    # resources opened can be closed automatically using WITH keyword while opening file
    with open("TryExcept.py") as file:
        print("file opened")
    age = int(input("age : "))
    xfactor = 10/age
except (ValueError,ZeroDivisionError):
    print("You didnt enter a valid age")
else:
    print("No exceptions are found.")