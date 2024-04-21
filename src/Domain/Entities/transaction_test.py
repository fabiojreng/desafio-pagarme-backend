import pytest
from .transaction import Transaction
from ..VO.Transaction.card_expiration import CardExpiration
from ..VO.Transaction.card_number import CardNumber
from ..VO.Transaction.payment_method import PaymentMethod


@pytest.fixture
def valid_transaction_data():
    return {
        "transaction_value": 100.0,
        "transaction_description": "description",
        "payment_method": "credit_card",
        "card_number": "1215 1531 5345 6548",
        "cardholder_name": "John Doe",
        "card_expiration": "12/24",
        "cvv": "123",
    }


def test_create_transaction(valid_transaction_data):
    transaction = Transaction.create(**valid_transaction_data)

    print(transaction.to_dict())
    assert transaction.get_transaction_value().get_value() == 100.0
    assert transaction.get_transaction_description().get_value() == "description"
    assert isinstance(transaction.get_payment_method(), PaymentMethod)
    assert transaction.get_payment_method().get_value() == "credit_card"
    assert isinstance(transaction.get_card_number(), CardNumber)
    assert transaction.get_card_number().get_value() == "6548"
    assert transaction.get_cardholder_name().get_value() == "John Doe"
    assert isinstance(transaction.get_card_expiration(), CardExpiration)
    assert transaction.get_card_expiration().get_value() == "12/24"
    assert transaction.get_cvv().get_value() == "123"


@pytest.fixture
def valid_transaction_data2():
    return {
        "id": "1234485437",
        "transaction_value": 100.0,
        "transaction_description": "description",
        "payment_method": "credit_card",
        "card_number": "1215 1531 5345 6548",
        "cardholder_name": "John Doe",
        "card_expiration": "12/24",
        "cvv": "123",
    }


def test_restore_transaction(valid_transaction_data2):
    transaction = Transaction.restore(**valid_transaction_data2)

    print(transaction.to_dict())
    assert transaction.get_transaction_value().get_value() == 100.0
    assert transaction.get_transaction_description().get_value() == "description"
    assert isinstance(transaction.get_payment_method(), PaymentMethod)
    assert transaction.get_payment_method().get_value() == "credit_card"
    assert isinstance(transaction.get_card_number(), CardNumber)
    assert transaction.get_card_number().get_value() == "6548"
    assert transaction.get_cardholder_name().get_value() == "John Doe"
    assert isinstance(transaction.get_card_expiration(), CardExpiration)
    assert transaction.get_card_expiration().get_value() == "12/24"
    assert transaction.get_cvv().get_value() == "123"
