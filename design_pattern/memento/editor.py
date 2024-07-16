from editor_state import EditorState


class Editor:
    def __init__(self):
        self.__content = None

    def get_content(self):
        return self.__content

    def set_content(self, content):
        self.__content = content

    def create_state(self):
        return EditorState(self.__content)

    def restore_state(self, state):
        self.__content = state.get_content()



