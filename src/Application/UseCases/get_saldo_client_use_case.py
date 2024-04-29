from src.Application.UseCases.interface_use_case import UseCaseInterface
from src.Domain.Repository.client_repository import ClientRepositoryInterface
from src.Domain.Repository.payable_repository import PayableRepositoryInterface
from src.Domain.Helpers.http_helper import (
    HttpResponse,
    forbidden,
    not_found,
    success,
    unprocessable_entity,
    server_error,
)


class GetSaldoClientUseCase(UseCaseInterface):
    def __init__(
        self,
        client_repository: ClientRepositoryInterface,
        payable_repository: PayableRepositoryInterface,
    ) -> None:
        self.__client_repository = client_repository
        self.__payable_repository = payable_repository

    def execute(self, params: any) -> HttpResponse:
        try:
            valid_params = ["Paid", "Waiting_funds"]
            if params["status"] not in valid_params:
                return forbidden("Invalid balance type")

            client = self.__client_repository.get_client_id(params["client_id"])
            if not client:
                return not_found("Client not found")

            payables = self.__payable_repository.get_payble_client(
                params["client_id"],
                params["status"],
            )

            if not payables:
                return success(
                    {
                        "message": "Client does not have a {} balance".format(
                            params["status"]
                        ),
                    }
                )

            values = [float(amount[2]) for amount in payables]
            saldo = 0.0
            for value in values:
                saldo += value

            return success(
                {
                    "message": "Saldo com status {}".format(params["status"]),
                    "data": {"client": client["name"], "saldo": saldo},
                }
            )

        except Exception as e:
            if isinstance(e, Exception):
                return unprocessable_entity(str(e))
            return server_error("Unexpected Error")
