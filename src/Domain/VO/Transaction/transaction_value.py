class TransactionValue:
    def __init__(self, transaction_value: float) -> None:
        if transaction_value <= 0:
            raise ValueError(
                "It is not possible to create a transaction with a negative or null value"
            )
        self.__transaction_value = transaction_value

    def get_value(self) -> float:
        return self.__transaction_value
