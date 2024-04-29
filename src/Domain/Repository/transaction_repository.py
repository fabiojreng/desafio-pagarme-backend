from abc import ABC, abstractmethod
from src.Domain.Entities.transaction import Transaction


class TransactionRepositoryInterface(ABC):
    @abstractmethod
    def save_transaction(self, transaction: Transaction) -> None:
        pass

    @abstractmethod
    def get_transaction_id(self, id: str) -> list:
        pass

    @abstractmethod
    def find_all_transactions(self) -> list[dict]:
        pass
