import pytest
from src.vacancies import Vacancies


@pytest.fixture
def test_vacancies():
    return Vacancies("python", 1)


def test_str(test_vacancies):
    """
    Проверка метода str
    """
    assert str(test_vacancies) == "python"


def test_repr(test_vacancies):
    """
    Проверка метода repr
    """
    assert repr(test_vacancies) == "Vacancies(('python', 1))"


def test_name_error(test_vacancies):
    """
    Проверка на наличие ошибок в названии
    """
    with pytest.raises(AttributeError):
        test_vacancies.name = "word"


def test_page_error(test_vacancies):
    """
    Проверка на наличие ошибок в количестве
    """
    with pytest.raises(AttributeError):
        test_vacancies.page = 1
