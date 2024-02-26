from abc import ABC, abstractmethod


class VacanciesAPI(ABC):
    """
    создан абстрактный класс для вакансий и его метода
    """
    @abstractmethod
    def get_vacancies(self):
        pass
