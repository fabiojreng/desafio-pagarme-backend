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

            return success({"message": "Transaction list", "data": transactions})

        except Exception as e:
            if isinstance(e, Exception):
                return unprocessable_entity(str(e))
            return server_error("Unexpected Error")
