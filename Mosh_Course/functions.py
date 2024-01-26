# Types of functions
# 1. Task performing functions
def greet(name):
    print(f"Hi {name}")

# 2. Value returning functions
def getGreet(name):
    return f"Hi {name}"

def increment(number, by):
    return number+by

print(increment(3,6))