from abc import ABC, abstractmethod
from src.Domain.Entities.client import Client


class ClientRepositoryInterface(ABC):
    @abstractmethod
    def save_client(self, client: Client) -> None:
        pass

    @abstractmethod
    def get_client_id(self, id: str) -> Client:
        pass

    @abstractmethod
    def get_client_email(self, email: str) -> Client:
        pass

    @abstractmethod
    def find_all_clients(self) -> list[dict]:
        pass
