class CVV:
    def __init__(self, cvv: str) -> None:
        cvv = cvv.replace(" ", "")
        if not cvv.isdigit():
            raise ValueError("Only numeric values ​​can be entered")
        if len(cvv) != 3:
            raise ValueError("Number of digits on the cvv is invalid")
        self.__cvv = cvv

    def get_value(self) -> str:
        return self.__cvv
