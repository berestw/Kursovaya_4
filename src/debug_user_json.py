from src.abstract_user_form import UserForm


class DebugUserJson(UserForm):
    """
    класс ввода ошибок зарплаты и города
    """
    payment = None
    town = None

    def user_input_int(self):
        """
        ошибки на ввод з/п
        :return:
        """
        self.payment = input("Введите минимальную з/п: ")
        if self.payment.isalpha():
            raise ValueError("З/п должно быть числом")
        if self.payment == "":
            self.payment = 0
        return int(self.payment)

    def user_input_str(self):
        """
        ошибки вводы города
        :return:
        """
        self.town = input("Введите нужный город: ").title()
        if self.town.isdigit():
            raise TypeError("Запрос не может содержать числа")
        return self.town


if __name__ == '__main__':
    r = DebugUserJson()
    print(r.user_input_int())
