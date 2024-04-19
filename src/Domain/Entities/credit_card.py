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
        self._payment_date = datetime.now() + timedelta(days=30)
        # client.get_saldo_waiting_funds = self._amount

    def calculate_amount(self, transaction_value):
        fee = 0.05 * transaction_value
        amount = transaction_value - fee
        return amount

    @staticmethod
    def create(transaction, client):
        payment_id = uuid.uuid4()
        return CreditCard(payment_id, transaction, client)

    @staticmethod
    def restore(payment_id, transaction, client):
        return CreditCard(payment_id, transaction, client)
