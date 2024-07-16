from observer import Observer
from subject import Subject

class DataSource(Subject):
    def __init__(self, val: int) -> None:
        super().__init__()
        self._val = val

    def get_val(self) -> int:
        return self._val

    def set_val(self, val: int) -> None:
        self._val = val
        self.notify_observers()

