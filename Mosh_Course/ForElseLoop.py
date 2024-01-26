condition = False

for numbers in range(3):
    print("Attempt")
    if condition:
        print("Successfull")
        break
else:
    print("Failed after 3 attempts")