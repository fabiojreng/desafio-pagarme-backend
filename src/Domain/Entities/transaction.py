from ..VO.payment_method import PaymentMethod
from ..VO.card_number import CardNumber
from ..VO.card_expiration import CardExpiration


class Transaction:
    def __init__(
        self,
        transaction_value: float,
        transaction_description: str,
        payment_method: PaymentMethod,
        card_number: CardNumber,
        cardholder_name: str,
        card_expiration: CardExpiration,
        cvv: int,
    ) -> None:
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
        transaction_description: str,
        payment_method: str,
        card_number: str,
        cardholder_name: str,
        card_expiration: str,
        cvv: int,
    ):
        return Transaction(
            transaction_value,
            transaction_description,
            PaymentMethod(payment_method),
            CardNumber(card_number),
            cardholder_name,
            CardExpiration(card_expiration),
            cvv,
        )

    def get_transaction_value(self):
        return self.__transaction_value

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
