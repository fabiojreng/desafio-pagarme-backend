from abc import ABC, abstractmethod
from src.Domain.Entities.payable import Payable


class PayableRepositoryInterface(ABC):
    @abstractmethod
    def save_payable(self, payable: Payable) -> None:
        pass

    @abstractmethod
    def get_payble_id(self, id: str) -> dict:
        pass

    @abstractmethod
    def find_all_payable(self) -> list[dict]:
        pass

    @abstractmethod
    def get_paybles_client(self, client_id, status) -> list[dict]:
        pass
