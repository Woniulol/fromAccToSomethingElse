class BrowserHistory:
    def __init__(self):
        self.__history = [ ]
        self.__index = 0

    def push(self, url):
        self.__history.append(url)

    def pop(self):
        if len(self.__history) > 0:
            return self.__history.pop()
        else:
            return None

    def get_history(self):
        return self.__history

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < len(self.__history):
            result = self.__history[self.__index]
            self.__index += 1
            return result
        else:
            raise StopIteration


