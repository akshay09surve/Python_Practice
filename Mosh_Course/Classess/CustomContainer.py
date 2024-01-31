class TagCloud:
    
    def __init__(self):
        self.__tags = {}

    def add(self,tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(),0) +1

    def __getitem__(self,tag):
        return self.__tags.get(tag.lower(),0)

    # This method to set the count of tag manually 
    def __setitem__(self,tag,count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)


cloud = TagCloud()
cloud["Java"] = 10 #Setitem method
len(cloud) #  
cloud.add("Python")
cloud.add("python")
cloud.add("JavaScript")
print(cloud)