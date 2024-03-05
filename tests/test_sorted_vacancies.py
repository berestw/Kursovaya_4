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


def test_error_vacancies_sorted():
    """
    Проверка на наличие ошибок
    """
    with pytest.raises(TypeError):
        SortedVacancies(10)
