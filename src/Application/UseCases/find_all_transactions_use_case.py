from src.Application.UseCases.interface_use_case import UseCaseInterface
from src.Domain.Repository.transaction_repository import TransactionRepositoryInterface
from src.Domain.Helpers.http_helper import (
    HttpResponse,
    success,
    server_error,
    unprocessable_entity,
)


class FindAllTransactionsUseCase(UseCaseInterface):
    def __init__(self, transaction_repository: TransactionRepositoryInterface) -> None:
        self.__transaction_repository = transaction_repository

    def execute(self, params: any) -> HttpResponse:
        try:
            transactions = self.__transaction_repository.find_all_transactions()
            if not transactions:
                return success({"message": "There are no transactions made"})
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

            return success({"message": "Transaction list", "data": output})

        except Exception as e:
            if isinstance(e, Exception):
                return unprocessable_entity(str(e))
            return server_error("Unexpected Error")
