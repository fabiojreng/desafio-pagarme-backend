class CardNumber:
    def __init__(self, number: str) -> None:
        number = number.replace(" ", "")
        if not number.isdigit():
            raise ValueError("Apenas valores numéricos podem ser inseridos")
        if len(number) != 16:
            raise ValueError("Quantidade de dígitos do cartão inválido.")
        self.__card_number = number[-4:]

    def get_value(self) -> str:
        return self.__card_number


card = CardNumber("1215 1531 5345 6548")
print(card.get_value())
