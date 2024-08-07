from datetime import datetime, timedelta
import uuid
from src.Domain.Entities.payable import Payable
from src.Domain.Entities.transaction import Transaction
from src.Domain.Entities.client import Client


class CreditCard(Payable):
    def __init__(
        self, payment_id: str, transaction: Transaction, client: Client
    ) -> None:
        super().__init__(payment_id, transaction, client)
        self._amount = self.calculate_amount(self._transaction_value)
        self._status = "Waiting_funds"
        self._payment_method = "credit_card"
        self._payment_date = datetime.now() + timedelta(days=30)

    def calculate_amount(self, transaction_value):
        fee = 0.05 * transaction_value
        amount = transaction_value - fee
        return amount

    @classmethod
    def create(cls, transaction, client):
        payment_id = uuid.uuid4()
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
