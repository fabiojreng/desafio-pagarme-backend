class CardNumber:
    def __init__(self, number: str) -> None:
        number = number.replace(" ", "")
        if not number.isdigit():
            raise ValueError("Only numeric values ​​can be entered")
        if len(number) != 16:
            raise ValueError("Number of digits on the card is invalid")
        self.__card_number = number[-4:]

    def get_value(self) -> str:
        return self.__card_number
