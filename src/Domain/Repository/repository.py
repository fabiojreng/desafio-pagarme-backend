from abc import ABC, abstractmethod
from src.Domain.Entities.payable import Payable
from src.Domain.Entities.transaction import Transaction
from src.Domain.Entities.client import Client


class RepositoryInterface(ABC):
    @abstractmethod
    def save_transaction(self, Transaction: Transaction) -> Transaction:
        pass

    @abstractmethod
    def find_all_transactions(self) -> list[Transaction]:
        pass

    @abstractmethod
    def find_all_payables(self) -> list[Payable]:
        pass

    @abstractmethod
    def get_transaction_id(self, id: str) -> Payable:
        pass

    @abstractmethod
    def get_client_id(self, id: str) -> Client:
        pass

    @abstractmethod
    def save_payable(self, payable: Payable) -> Payable:
        pass

    @abstractmethod
    def save_client(self, client: Client):
        pass
