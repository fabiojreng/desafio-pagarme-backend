from abc import ABC, abstractmethod
from src.Domain.Entities.client import Client


class ClientRepositoryInterface(ABC):
    @abstractmethod
    def save_client(self, client: Client):
        pass

    @abstractmethod
    def get_client_id(self, id: str):
        pass

    @abstractmethod
    def get_client_email(self, email: str):
        pass

    @abstractmethod
    def find_all_clients(self):
        pass
