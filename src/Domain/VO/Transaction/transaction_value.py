class TransactionValue:
    def __init__(self, transaction_value: float) -> None:
        if transaction_value <= 0:
            raise ValueError(
                "Não é possível criar transação com valor negativo ou nulo"
            )
        self.__transaction_value = transaction_value

    def get_value(self) -> float:
        return self.__transaction_value
