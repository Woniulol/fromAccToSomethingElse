from observer import Observer
from data_source import DataSource

class Chart(Observer):
    def __init__(self, data_source: DataSource):
        self._data_source = data_source

    def update(self):
        val = self._data_source.get_val()
        print(f"Chart is updated. {val}")
