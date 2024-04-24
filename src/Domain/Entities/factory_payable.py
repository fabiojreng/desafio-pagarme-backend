from src.Domain.Entities.credit_card import CreditCard
from src.Domain.Entities.debit_card import DebitCard


class FactoryPayable:
    def create(transaction, client):
        if transaction["payment_method"] == "debit_card":
            return DebitCard.create(transaction, client).to_dict()
        elif transaction["payment_method"] == "credit_card":
            return CreditCard.create(transaction, client).to_dict()
        else:
            raise ValueError("Invalid payment type")
