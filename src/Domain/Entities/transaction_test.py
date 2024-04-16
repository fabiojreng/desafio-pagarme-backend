import pytest
from .transaction import Transaction
from ..VO.card_expiration import CardExpiration
from ..VO.card_number import CardNumber
from ..VO.payment_method import PaymentMethod


@pytest.fixture
def valid_transaction_data():
    return {
        "transaction_value": 100.0,
        "transaction_description": "description",
        "payment_method": "credit_card",
        "card_number": "3456",
        "cardholder_name": "John Doe",
        "card_expiration": "12/2025",
        "cvv": 123,
    }


def test_create_transaction(valid_transaction_data):
    transaction = Transaction.create(**valid_transaction_data)

    assert transaction.get_transaction_value() == 100.0
    assert transaction.get_transaction_description() == "description"
    assert isinstance(transaction.get_payment_method(), PaymentMethod)
    assert transaction.get_payment_method().get_value() == "credit_card"
    assert isinstance(transaction.get_card_number(), CardNumber)
    assert transaction.get_card_number().get_value() == "3456"
    assert transaction.get_cardholder_name() == "John Doe"
    assert isinstance(transaction.get_card_expiration(), CardExpiration)
    assert transaction.get_card_expiration().get_value() == "12/2025"
    assert transaction.get_cvv() == 123
