from datetime import datetime
import pytest
from .transaction import Transaction
from .client import Client
from .debit_card import DebitCard
from .payable import Payable
from .credit_card import CreditCard


@pytest.fixture
def sample_transaction():
    return Transaction(
        "12345678",
        100.0,
        "description",
        "credit_card",
        "1215 1531 5345 6548",
        "John Doe",
        "12/24",
        "123",
    )


@pytest.fixture
def sample_client():
    return Client("1234", "Jonh Doe", "johndoe@email.com")


def test_debit_card_creation(sample_transaction, sample_client):
    debit_card = DebitCard.create(sample_transaction, sample_client)

    assert isinstance(debit_card, DebitCard)
    assert isinstance(debit_card, Payable)
    assert debit_card._status == "Paid"
    print()
    print(debit_card._payment_date)
    assert isinstance(debit_card._payment_date, datetime)
    assert debit_card._amount == 97
    assert debit_card._client_name == "Jonh Doe"


def test_credit_card_creation(sample_transaction, sample_client):
    credit_card = CreditCard.create(sample_transaction, sample_client)

    assert isinstance(credit_card, CreditCard)
    assert isinstance(credit_card, Payable)
    assert credit_card._status == "Waiting_funds"
    print()
    print(credit_card._payment_date)
    assert isinstance(credit_card._payment_date, datetime)
    assert credit_card._amount == 95
    assert credit_card._client_name == "Jonh Doe"
