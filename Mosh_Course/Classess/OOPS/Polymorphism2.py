from abc import ABC, abstractmethod

class UIControl(ABC):

    @abstractmethod
    def draw(self):
        pass


class Textbox(UIControl):

    def draw(self):
        print("Textbox")


class DropDownList(UIControl):

    def draw(self):
        print("DropDownList")


def draw(controls):

    for control in controls:
        control.draw()


tb = Textbox()
ddl = DropDownList()
draw([tb,ddl])
