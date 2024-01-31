class Text(str):

    def duplicate(self):
        return self + self
    

txt = Text("Python")
print(txt.lower())

print(txt.duplicate())


class TrackableList(list):

    def append(self, __object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append("1")