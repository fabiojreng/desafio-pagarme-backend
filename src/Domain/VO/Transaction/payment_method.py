class PaymentMethod:
    def __init__(self, method: str) -> None:
        valid_methods = ["debit_card", "credit_card"]
        if method not in valid_methods:
            raise ValueError(
                "Método de pagamento inválido. Use 'credit_card' ou 'debit_card'."
            )
        self.__payment_method = method

    def get_value(self) -> str:
        return self.__payment_method
