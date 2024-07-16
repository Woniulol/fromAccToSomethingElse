from observer import Observer
from data_source import DataSource

class SpreadSheet(Observer):
    def __init__(self, data_source: DataSource):
        self._data_source = data_source

    def update(self):
        val = self._data_source.get_val()
        print(f"SpreadSheet is updated. {val}")