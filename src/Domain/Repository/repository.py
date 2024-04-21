from abc import ABC, abstractmethod
from src.Domain.Entities.payable import Payable
from src.Domain.Entities.transaction import Transaction


class RepositoryInterface(ABC):
    @abstractmethod
    def save_transaction(self, Transaction: Transaction) -> Transaction:
        pass

    @abstractmethod
    def findAll(self) -> list[Transaction]:
        pass

    @abstractmethod
    def get_transaction_id(self, id: str):
        pass

    @abstractmethod
    def get_client_id(self, id: str):
        pass

    @abstractmethod
    def save_payable(self, payable: Payable) -> Payable:
        pass
