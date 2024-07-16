from observer import Observer
from abc import ABC, abstractmethod


class Subject(ABC):
    def __init__(self) -> None:
        self._observers: list[Observer] = [ ]

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()
