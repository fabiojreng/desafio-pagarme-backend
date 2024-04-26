from src.Application.UseCases.interface_use_case import UseCaseInterface
from src.Domain.Repository.client_repository import ClientRepositoryInterface
from src.Domain.Repository.payable_repository import PayableRepositoryInterface


class GetSaldoClientUseCase(UseCaseInterface):
    def __init__(
        self,
        client_repository: ClientRepositoryInterface,
        payable_repository: PayableRepositoryInterface,
    ) -> None:
        self.__client_repository = client_repository
        self.__payable_repository = payable_repository

    def execute(self, params):
        try:
            client = self.__client_repository.get_client_id(params["client_id"])
            if not client:
                return {
                    "status_code": 404,
                    "body": "Client not found",
                }
            payables = self.__payable_repository.get_payble_client(
                params["client_id"],
                params["status"],
            )

            if not payables:
                return {
                    "status_code": 200,
                    "body": "client does not have a {} balance".format(
                        params["status"]
                    ),
                }

            values = [float(amount[2]) for amount in payables]
            amount = 0.0
            for value in values:
                amount += value

            return {
                "status_code": 200,
                "body": {"status": params["status"], "amount": amount},
            }

        except Exception as e:
            if isinstance(e, Exception):
                return {
                    "status_code": 422,
                    "body": str(e),
                }
            return {
                "status_code": 500,
                "body": "Unexpected Error",
            }
