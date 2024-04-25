from datetime import datetime
import uuid
from src.Domain.Entities.payable import Payable
from src.Domain.Entities.transaction import Transaction
from src.Domain.Entities.client import Client


class DebitCard(Payable):
    def __init__(
        self, payment_id: str, transaction: Transaction, client: Client
    ) -> None:
        super().__init__(payment_id, transaction, client)
        self._amount = self.calculate_amount(self._transaction_value)
        self._status = "Paid"
        self._payment_method = "debit_card"
        self._payment_date = datetime.now()
        # client.__saldo_available = self._amount

    def calculate_amount(self, transaction_value):
        fee = 0.03 * transaction_value
        amount = transaction_value - fee
        return amount

    @classmethod
    def create(cls, transaction, client):
        payment_id = uuid.uuid4()
        return cls(payment_id, transaction, client)

    @classmethod
    def restore(cls, payment_id, transaction, client):
        return cls(payment_id, transaction, client)

    def to_dict(self):
        return {
            "amount": self._amount,
            "payment_method": self._payment_method,
            "card_number": self._card_number,
            "payment_id": str(self._id),
            "status": self._status,
            "client_id": self._client_id,
            "payment_date": self._payment_date,
        }
