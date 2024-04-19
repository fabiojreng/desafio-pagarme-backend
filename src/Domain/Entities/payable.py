from abc import ABC, abstractmethod
from src.Domain.Entities.transaction import Transaction
from src.Domain.Entities.client import Client


class Payable(ABC):

    def __init__(
        self, payment_id: str, transaction: Transaction, client: Client
    ) -> None:
        self._id = payment_id
        self._amount = None
        self._transaction_value = transaction.get_transaction_value()
        self._client_name = client.get_name()
        self._status = None
        self._payment_date = None

    @abstractmethod
    def calculate_amount(self, transaction_value):
        pass

    @abstractmethod
    def create(transaction, client):
        pass

    @abstractmethod
    def restore(payment_id, transaction, client):
        pass
