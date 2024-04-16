from datetime import datetime


class CardExpiration:
    def __init__(self, date_expiration: str) -> None:
        self.__expiration_date = self.__expiration_date(date_expiration)

    def __expiration_date(self, expiration: str) -> datetime:
        try:
            expiration_date = datetime.strptime(expiration, "%m/%Y")
            if expiration_date < datetime.now():
                raise ValueError("A data de expiração não pode ser no passado.")
            return expiration_date.strftime("%m/%Y")
        except ValueError:
            raise ValueError(
                "Formato de data de expiração inválido. Use o formato MM/YYYY."
            )

    def get_value(self) -> str:
        return self.__expiration_date
