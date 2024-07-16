from editor_state import EditorState

class EditorHistory:
    def __init__(self) -> None:
        self.__history: list[EditorState] = [ ]

    def push(self, editor_state):
        self.__history.append(editor_state)

    def pop(self):
        if len(self.__history) > 0:
            return self.__history.pop()
        else:
            return None
