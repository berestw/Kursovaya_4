from src.hh_requests_debug import HhRequestsDebug
from src.debug_user_json import DebugUserJson
from src.sorted_vacancies import SortedVacancies
from src.connection_hh import GetHeadHunter


class UserInteractionHeadHunter(HhRequestsDebug):
    """
    Класс взаимодействия пользователя с сайтом HeadHunter
    """
    def hh_user_search(self):
        search_query = self.user_input_str()
        top_n = self.user_input_int()
        result_search = GetHeadHunter(search_query, top_n)
        result_search.get_json()


class UserInteractionJson(DebugUserJson):
    """
    Класс взаимодействия пользователя с файлом Json
    """
    def json_user_search(self):
        """
        Метод сортировки вакансий Json файла
        """
        vacancies_list = []
        json_file = SortedVacancies()
        json_vacancies = json_file.sorted_vacancies_hh
        payment = self.user_input_int()
        town = self.user_input_str()
        for vacancies in json_vacancies:
            if payment > vacancies["payment_from"]:
                continue
            if town == vacancies["town"]:
                vacancies_list.append(vacancies)
            if town == "":
                vacancies_list.append(vacancies)
        for result in vacancies_list:
            print(f"Город: {result['town']}\nДата публикации: {result['date']}\n"
                  f"Должность: {result['name']}\nТребование: {result['requirement']}\n"
                  f"Ответственность: {result['responsibility']}\nЗарплата от {result['payment_from']}\n"
                  f"Зарплата до {result['payment_to']}\n")
        if len(vacancies_list) == 0:
            print(f'Результатов 0')


if __name__ == '__main__':
    r = UserInteractionHeadHunter()
    r.hh_user_search()
