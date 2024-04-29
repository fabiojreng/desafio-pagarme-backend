import uuid
from src.Domain.Entities.client import Name
from src.Domain.VO.Transaction.card_expiration import CardExpiration
from src.Domain.VO.Transaction.card_number import CardNumber
from src.Domain.VO.Transaction.cvv import CVV
from src.Domain.VO.Transaction.payment_method import PaymentMethod
from src.Domain.VO.Transaction.transaction_description import TransactionDescription
from src.Domain.VO.Transaction.transaction_value import TransactionValue


class Transaction:
    def __init__(
        self,
        transaction_id: str,
        transaction_value: TransactionValue,
        client_id: str,
        transaction_description: TransactionDescription,
        payment_method: PaymentMethod,
        card_number: CardNumber,
        cardholder_name: Name,
        card_expiration: CardExpiration,
        cvv: CVV,
    ) -> None:
        self.__transaction_id = transaction_id
        self.__client_id = client_id
        self.__transaction_value = transaction_value
        self.__transaction_description = transaction_description
        self.__payment_method = payment_method
        self.__card_number = card_number
        self.__cardholder_name = cardholder_name
        self.__card_expiration = card_expiration
        self.__cvv = cvv

    @staticmethod
    def create(
        transaction_value: float,
        client_id: str,
        transaction_description: str,
        payment_method: str,
        card_number: str,
        cardholder_name: str,
        card_expiration: str,
        cvv: str,
    ):
        transaction_id = uuid.uuid4()
        return Transaction(
            transaction_id,
            TransactionValue(transaction_value),
            client_id,
            TransactionDescription(transaction_description),
            PaymentMethod(payment_method),
            CardNumber(card_number),
            Name(cardholder_name),
            CardExpiration(card_expiration),
            CVV(cvv),
        )

    def to_dict(self):
        return {
            "transaction_id": str(self.__transaction_id),
            "transaction_value": self.__transaction_value.get_value(),
            "client_id": self.__client_id,
            "transaction_description": self.__transaction_description.get_value(),
            "payment_method": self.__payment_method.get_value(),
            "card_number": self.__card_number.get_value(),
            "cardholder_name": self.__cardholder_name.get_value(),
            "card_expiration": self.__card_expiration.get_value(),
            "cvv": self.__cvv.get_value(),
        }

    def get_transaction_id(self):
        return self.__transaction_id

    def get_transaction_value(self):
        return self.__transaction_value

    def get_client_id(self):
        return self.__client_id

    def get_transaction_description(self):
        return self.__transaction_description

    def get_cardholder_name(self):
        return self.__cardholder_name

    def get_card_expiration(self):
        return self.__card_expiration

    def get_card_number(self):
        return self.__card_number

    def get_payment_method(self):
        return self.__payment_method

    def get_cvv(self):
        return self.__cvv
