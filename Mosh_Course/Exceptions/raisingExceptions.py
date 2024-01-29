from timeit import timeit

code1="""
def calculate_Xfactor(age):
    if age <=0:
        raise ValueError("Age can not be zero or less.")
    return 10/age


try:
    calculate_Xfactor(-1)
except ValueError as error:
    print(error)
"""

code2="""
def calculate_Xfactor(age):
    if age <=0:
        return None
    return 10/age


xfactor = calculate_Xfactor(-1)
if xfactor == None:
    pass
"""

print("First code : ",timeit(code1, number=10000))
print("Second code : ",timeit(code2, number=10000))