from datetime import datetime


class CardExpiration:
    def __init__(self, date_expiration: str) -> None:
        self.__expiration_date = self.__verify_expiration_date(date_expiration)

    def __verify_expiration_date(self, expiration: str) -> datetime:
        expiration = expiration.replace(" ", "")
        try:
            expiration_date = datetime.strptime(expiration, "%m/%y")
            if expiration_date < datetime.now():
                raise ValueError("A data de expiração não pode ser no passado.")
            return expiration_date.strftime("%m/%y")
        except ValueError as e:
            raise ValueError(str(e))

    def get_value(self) -> str:
        return self.__expiration_date
