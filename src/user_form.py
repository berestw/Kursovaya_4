from abc import ABC, abstractmethod


class UserForm(ABC):
    """
    создание абстракного класса для user и его методов
    """
    @abstractmethod
    def user_input_int(self):
        pass

    @abstractmethod
    def user_input_str(self):
        pass
