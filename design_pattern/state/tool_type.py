from abc import ABC, abstractmethod

class ToolType(ABC):
    @abstractmethod
    def mouse_down(self):
        ...

class Pen(ToolType):
    def mouse_down(self):
        print("Pen: mouse down")


class Pencil(ToolType):
    def mouse_down(self):
        print("Pencil: mouse down")


class Eraser(ToolType):
    def mouse_down(self):
        print("Eraser: mouse down")