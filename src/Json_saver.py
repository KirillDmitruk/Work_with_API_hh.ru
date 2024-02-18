import json
from config import DATA
from src.Abstract_class_json import AbstractJson


class JsonSaver(AbstractJson):

    def save_file(self, data: list):
        """Сохраняет данные в json"""
        with open(DATA, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, indent=4, ensure_ascii=False))

    def read_file(self):
        """Cчитывает данные из файла json и возвращает их в виде списка"""
        with open(DATA, encoding='utf-8') as file:
            return json.load(file)

    def add_vacancy_to_file(self, data: list):
        """Добавляет новый список вакансий в файл json"""
        old_list = self.read_file()
        new_list = data + old_list
        self.save_file(new_list)

    def delete_vacancy(self, vacancy: str):
        """Удаляет вакансию из файла json"""
        new_list = []

        old_list = self.read_file()

        for params in old_list:
            if params['name'] != vacancy:
                new_list.append(params)

        self.save_file(new_list)
