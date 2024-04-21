import uuid
from src.Domain.VO.Client.name import Name
from src.Domain.VO.Client.email import Email


class Client:
    def __init__(self, id: str, name: Name, email: Email) -> None:
        self.__id = id
        self.__name = name
        self.__email = email
        self.__saldo_available: float
        self.__saldo_waiting_funds: float

    @staticmethod
    def create(name: str, email: str):
        id = uuid.uuid4()
        return Client(id, Name(name), Email(email))

    @staticmethod
    def restore(id, name: str, email: str):
        return Client(id, Name(name), Email(email))

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_saldo_available(self):
        return self.__saldo_available

    def get_saldo_waiting_funds(self):
        return self.__saldo_waiting_funds
