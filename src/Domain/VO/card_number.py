class CardNumber:
    def __init__(self, number: str) -> None:
        if int(number) < 4:
            raise ValueError(
                "Número do cartão inválido. Deve ter pelo menos 4 dígitos."
            )
        self.__card_number = number[-4:]

    def get_value(self) -> str:
        return self.__card_number
