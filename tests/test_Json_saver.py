from abc import ABC

from src.Abstract_class_json import AbstractJsonSaver
from src.Json_saver import JsonSaver
from tests.test_fixture import fixture_class_json_saver, fixture_class_list

def test_json_saver_issubclass():
    assert issubclass(JsonSaver, AbstractJsonSaver)
    assert issubclass(AbstractJsonSaver, ABC)


def test_save_file_read_file(fixture_class_json_saver):
    fixture_class_json_saver.save_file([{'name': 'Kirill'}])

    assert isinstance(fixture_class_json_saver.read_file(), list)
    assert fixture_class_json_saver.read_file() == [{'name': 'Kirill'}]


def test_add_vacancy_to_file_and_delete(fixture_class_list):
    fixture_class_list.add_vacancy_to_file([{'name': 'Not Kirill'}])

    assert fixture_class_list.read_file() == [{'name': 'Not Kirill'}, {'name': 'Kirill'}]

    fixture_class_list.delete_vacancy('Kirill')
    assert fixture_class_list.read_file() == [{'name': 'Not Kirill'}]