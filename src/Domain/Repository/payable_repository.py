from abc import ABC, abstractmethod
from src.Domain.Entities.payable import Payable


class PayableRepositoryInterface(ABC):
    @abstractmethod
    def save_payable(self, payable: Payable):
        pass

    @abstractmethod
    def get_payble_id(self, id: str):
        pass

    @abstractmethod
    def find_all_payable(self):
        pass

    @abstractmethod
    def get_payble_client(self, client_id, status):
        pass
