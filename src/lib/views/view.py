from abc import abstractmethod


class View:
    def __init__(self):
        self.size = ()

    @abstractmethod
    def update(self): ...