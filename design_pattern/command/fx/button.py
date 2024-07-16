class Button:
    def __init__(self, label, command) -> None:
        self._label = label
        self._command = command

    def get_label(self):
        return self._label

    def set_label(self, label):
        self._label = label

    def click(self):
        # The operation being performed by the button may not have
        # known when build this class
        self._command.execute()
