import pytest
from src.connection_hh import GetHeadHunter
from src.sorted_vacancies import SortedVacancies


@pytest.fixture
def get_head_hunter():
    return GetHeadHunter("python", 1)


def test_sorted_vacancy():
    """
    Проверка на наличие 2х экземпляров класса
    """
    r = SortedVacancies()
    assert r.head_hunter_sorted == []
    assert r.date_format == None


def test_sorted_vacancies_hh():
    """
     Проверка на работоспособность сортировки вакансии
    """
    r = SortedVacancies()
    assert r.sorted_vacancies_hh == [{'town': 'Оренбург',
                                      'date': '29.01.2024',
                                      'name': 'Стажер-разработчик Python',
                                      'payment_from': 50000,
                                      'payment_to': 50000,
                                      'requirement': 'Отличные коммуникативные навыки. Любовь к коду. Быть активным и '
                                                     'внедрять эффективные решения.',
                                      'responsibility': 'Внедрять новые инженерные решения. Поддерживать текущий '
                                                        'проект.'
                                                        'Разработка десктоп ПО по нашим лекалам.'}]


def test_error_vacancies_sorted():
    """
    Проверка на наличие ошибок
    """
    with pytest.raises(TypeError):
        SortedVacancies(10)
