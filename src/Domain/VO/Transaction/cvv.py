class CVV:
    def __init__(self, cvv: str) -> None:
        cvv = cvv.replace(" ", "")
        if not cvv.isdigit():
            raise ValueError("Apenas valores numéricos podem ser inseridos")
        if len(cvv) != 3:
            raise ValueError("Quantidade de dígitos inválida")
        self.__cvv = cvv

    def get_value(self) -> str:
        return self.__cvv
