class TransactionDescription:
    def __init__(self, description: str) -> None:
        max_words = 5
        num_words = len(description.split())
        if max_words < num_words:
            raise ValueError(f"A descrição deve conter no máximo {max_words} palavras.")
        self.__description = description

    def get_value(self):
        return self.__description
