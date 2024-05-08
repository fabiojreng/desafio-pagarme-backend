import uuid
from src.Domain.VO.Client.name import Name
from src.Domain.VO.Client.email import Email


class Client:
    def __init__(self, id: str, name: Name, email: Email) -> None:
        self.__id = id
        self.__name = name
        self.__email = email

    @staticmethod
    def create(name: str, email: str):
        id = uuid.uuid4()
        return Client(id, Name(name), Email(email))

    @staticmethod
    def restore(id, name: str, email: str):
        return Client(id, Name(name), Email(email))

    def to_dict(self):
        return {
            "id": str(self.__id),
            "name": self.__name.get_value(),
            "email": self.__email.get_value(),
        }

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name.get_value()

    def get_email(self):
        return self.__email.get_value()
