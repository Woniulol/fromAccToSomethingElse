from abc import ABC, abstractmethod

class Filter(ABC):
    @abstractmethod
    def filter(self, data):
        ...

class BlackAndWhiteFilter(Filter):
    def filter(self, data):
        print("filter black and white")

class GrayScaleFilter(Filter):
    def filter(self, data):
        print("filter gray scale")