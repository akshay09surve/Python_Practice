# class Employee:

#     def greet(self):
#         print("Employee greets.")

# class Person:

#     def greet(self):
#         print("Person greets.")

# class Manager(Employee, Person):
#     pass

# manager = Manager()
# manager.greet()

class InvalidOperationError(Exception):
    pass

class Stream:

    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False


class FileStream(Stream):

    def read(self):
        print("Reading data from a file.")


class NetworkStream(Stream):
    
    def read(self):
        print("Reading data from a network.")

