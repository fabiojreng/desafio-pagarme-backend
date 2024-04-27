from src.Application.UseCases.interface_use_case import UseCaseInterface
from src.Domain.Repository.transaction_repository import TransactionRepositoryInterface


class FindAllTransactionsUseCase(UseCaseInterface):
    def __init__(self, transaction_repository: TransactionRepositoryInterface) -> None:
        self.__transaction_repository = transaction_repository

    def execute(self, params):
        try:
            transactions = self.__transaction_repository.find_all_transactions()
            if transactions:
                output = [
                    {
                        "transaction_id": transaction[0],
                        "transaction_value": float(transaction[1]),
                        "client_id": transaction[2],
                        "transaction_description": transaction[3],
                        "payment_method": transaction[4],
                        "card_number": transaction[5],
                        "cardholder_name": transaction[6],
                        "card_expiration": transaction[7],
                        "cvv": transaction[8],
                    }
                    for transaction in transactions
                ]

            return {"status_code": 200, "body": output}

        except Exception as e:
            if isinstance(e, Exception):
                return {"status_code": 422, "body": str(e)}
            return {"status_code": 500, "body": "Unexpected Error"}
