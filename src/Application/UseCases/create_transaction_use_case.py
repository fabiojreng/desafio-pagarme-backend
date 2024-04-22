from src.Application.UseCases.interface_use_case import UseCaseInterface
from src.Domain.Entities.transaction import Transaction
from src.Domain.Repository.repository import RepositoryInterface


class CreateTransactionUseCase(UseCaseInterface):

    def __init__(self, repository: RepositoryInterface) -> None:
        self.__repository = repository

    async def execute(self, params):
        try:
            transaction = Transaction.create(
                params["transaction_value"],
                params["transaction_description"],
                params["payment_method"],
                params["card_number"],
                params["cardholder_name"],
                params["card_expiration"],
                params["cvv"],
            ).to_dict()
            await self.__repository.save_transaction(transaction)
            return transaction
        except Exception as e:
            return str(e)
