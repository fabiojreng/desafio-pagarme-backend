from datetime import datetime


class CardExpiration:
    def __init__(self, date_expiration: str) -> None:
        self.__expiration_date = self.__verify_expiration_date(date_expiration)

    def __verify_expiration_date(self, expiration: str) -> datetime:
        expiration = expiration.replace(" ", "")
        expiration_date = datetime.strptime(expiration, "%m/%y")
        if expiration_date < datetime.now():
            raise ValueError("The expiration date cannot be in the past")
        return expiration_date.strftime("%m/%y")

    def get_value(self) -> str:
        return self.__expiration_date
