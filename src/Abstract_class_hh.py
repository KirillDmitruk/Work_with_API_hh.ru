from abc import ABC, abstractmethod


class Abstract_class_hh(ABC):

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_vacancies_from_hh(self, name_vacancy):
        pass

