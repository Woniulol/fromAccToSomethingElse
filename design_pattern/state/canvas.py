from tool_type import ToolType

class Canvas:
    def __init__(self, cur_tool: ToolType | None = None):
        self.__cur_tool = cur_tool

    def set_tool(self, tool):
        self.__cur_tool = tool

    def get_tool(self):
        return self.__cur_tool

    def mouse_down(self):
        # mouse down event should be handled by the current tool
        self.__cur_tool.mouse_down()