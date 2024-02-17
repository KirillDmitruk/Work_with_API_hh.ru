from abc import ABC, abstractmethod

class AbstractJson(ABC):

    @abstractmethod
    def read_file(self):
        pass

    def save_file(self, data):
        pass