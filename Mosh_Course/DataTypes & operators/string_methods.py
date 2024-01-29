course = "  python programming         "
# upper method turns whole string in uppercase
print(course.upper())
# lower method turns whole string in lowercase
print(course.lower())
# title method gives each word's first letter in capital
print(course.title())
# strip method removes any white space at the start and end of the string
print(course.strip())
print(course.lstrip())
print(course.rstrip())
# find method is used to find the index of character within string
print(course.find("pro"))
# replace method is used to replace a substring or characeter with other substring or character
print(course.replace("programm", "learn"))
# in method return boolean expression if perticular substring is found in string otherwise returns false
print("py" in course)
print("ny" in course)
# not in method is the exact opposite of 'in' method
print("ny" not in course)