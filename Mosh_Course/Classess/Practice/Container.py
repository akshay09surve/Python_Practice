class ContainerLearn:

    def __init__(self):
        self.tags = {}

    # To return the length of container
    def __len__(self):
        return len(self.tags)
    
    # To add objects to this container
    def add(self,tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(),0) + 1
        return "Key-value Object added"

    # To set the object value manually
    def __setitem__(self,tag,count):
        self.tags[tag.lower()] = count

    # To get the object 
    def __getitem__(self,tag):
        return self.tags.get(tag.lower(),0)
    
    # To delete all the objects in dictionary
    def clear(self):
        self.tags = {}

    # To print all of the objects
    def __str__(self):
        return str(self.tags)
    
    # To delete one object
    def __delitem__(self,tag):
        try:
            self.tags.__delitem__(tag.lower())
        except KeyError:
            print(f"{tag} not found.")

    def __iter__(self):
        return iter(self.tags)

con = ContainerLearn()
con.add("Java") # To add new object
con.add("JavaScript")
con.add("Python")
print(con)
print(len(con)) # To get the count of total objects
#con.clear() # To delete all the objects
con.__delitem__("PHP")
print(con)
print(con.__iter__())