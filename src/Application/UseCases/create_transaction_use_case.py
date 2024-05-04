from src.Application.UseCases.interface_use_case import UseCaseInterface
from src.Domain.Entities.transaction import Transaction
from src.Domain.Repository.transaction_repository import TransactionRepositoryInterface
from src.Domain.Repository.client_repository import ClientRepositoryInterface
from src.Domain.Entities.factory_payable import FactoryPayable
from src.Domain.Repository.payable_repository import PayableRepositoryInterface
from src.Domain.Helpers.http_helper import (
    HttpResponse,
    not_found,
    created,
    server_error,
    unprocessable_entity,
)


class CreateTransactionUseCase(UseCaseInterface):

    def __init__(
        self,
        transaction_repository: TransactionRepositoryInterface,
        client_repository: ClientRepositoryInterface,
        payable_repository: PayableRepositoryInterface,
    ) -> None:
        self.__transaction_repository = transaction_repository
        self.__client_repository = client_repository
        self.__payble_repository = payable_repository

    def execute(self, params: any = None) -> HttpResponse:
        try:
            client = self.__client_repository.get_client_id(params["client_id"])
            if not client:
                return not_found("Client not found")

            transaction = Transaction.create(
                params["transaction_value"],
                params["client_id"],
                params["transaction_description"],
                params["payment_method"],
                params["card_number"],
                params["cardholder_name"],
                params["card_expiration"],
                params["cvv"],
            ).to_dict()

            payable = FactoryPayable.create(transaction, client)
            self.__transaction_repository.save_transaction(transaction)
            self.__payble_repository.save_payable(payable)

            return created(
                {
                    "message": "Transaction created successfully",
                    "data": {
                        "amount": round(payable["amount"], 2),
                        "payment_method": payable["payment_method"],
                        "card_number": payable["card_number"],
                        "payment_id": payable["payment_id"],
                    },
                }
            )
        except Exception as e:
            if isinstance(e, Exception):
                return unprocessable_entity(str(e))
            return server_error("Unexpected Error")
