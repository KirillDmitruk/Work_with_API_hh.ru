import json
from abc import ABC

import requests

from src.Abstract_class_hh import Abstract_class_hh


class Get_API_hh(Abstract_class_hh, ABC):

    def __init__(self):
        """
        Создаем пустой список all_vacancy,
        который будет использоваться для хранения информации о вакансиях.
        """
        self.all_vacancy = []

    def __repr__(self):
        """
        Метод возвращает строку, содержащую все вакансии, которые были получены.
        """
        return f"{self.all_vacancy}"

    def get_vacancy_from_api(self, name_vacancy) -> list:
        """
        Метод получает информацию о вакансиях с помощью API hh.ru.

        """
        if name_vacancy.isalpha():
            keys_response = {'text': f'name:{name_vacancy}', 'area': 113, 'per_page': 100, }
            info = requests.get(f'https://api.hh.ru/vacancies', keys_response)
            self.all_vacancy = json.loads(info.text)['items']
            return self.all_vacancy
        else:
            return "Vacancy not found"


