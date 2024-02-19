from src.Vacancy import Vacancy
from tests.test_fixture import new_file


def test_get_vacancy_list(new_file):
    vacancy = Vacancy.get_vacancy_list(new_file, 'Москва', 50000)
    vacancy2 = Vacancy.get_vacancy_list(new_file, 'Москва', 0)
    false_expected = vacancy < vacancy2
    assert false_expected == False
    assert len(vacancy) == 4
    assert len(vacancy[:2]) == 2