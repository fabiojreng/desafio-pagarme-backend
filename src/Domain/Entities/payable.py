from abc import ABC, abstractmethod
from src.Domain.Entities.transaction import Transaction
from src.Domain.Entities.client import Client


class Payable(ABC):

    def __init__(
        self, payment_id: str, transaction: Transaction, client: Client
    ) -> None:
        self._id = payment_id
        self._amount = None
        self._transaction_value = transaction["transaction_value"]
        self._transaction_id = transaction["transaction_id"]
        self._card_number = transaction["card_number"]
        self._client_name = client["name"]
        self._client_id = client["id"]
        self._status = None
        self._payment_date = None

    @abstractmethod
    def calculate_amount(self, transaction_value):
        pass

    @abstractmethod
    def create(cls, transaction, client):
        pass
