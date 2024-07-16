from editor import Editor
from editor_state import EditorState
from editor_his import EditorHistory

if __name__ == '__main__':
    editor = Editor()
    editor_his = EditorHistory()

    editor.set_content("hello world")
    editor_his.push(EditorState(editor.get_content()))

    editor.set_content("hello world * 2")
    editor_his.push(EditorState(editor.get_content()))

    editor.set_content("hello world * 3")
    editor.restore_state(state=editor_his.pop())
    editor.restore_state(state=editor_his.pop())

    print(editor.get_content())
