from tool_type import Pen, Pencil, Eraser
from canvas import Canvas

if __name__ == '__main__':
    canvas = Canvas()

    canvas.set_tool(Pen())
    canvas.mouse_down()

    canvas.set_tool(Pencil())
    canvas.mouse_down()

    canvas.set_tool(Eraser())
    canvas.mouse_down()