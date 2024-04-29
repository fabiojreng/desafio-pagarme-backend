from src.Domain.Repository.payable_repository import PayableRepositoryInterface
from src.Application.UseCases.interface_use_case import UseCaseInterface
from src.Domain.Helpers.http_helper import (
    HttpResponse,
    not_found,
    success,
    unprocessable_entity,
    server_error,
)


class GetPayableById(UseCaseInterface):
    def __init__(self, payable_repository: PayableRepositoryInterface) -> None:
        self.__payable_repository = payable_repository

    def execute(self, params: any) -> HttpResponse:
        try:
            payable = self.__payable_repository.get_payble_id(params["payable_id"])
            if not payable:
                return not_found("Payable not found")
            id, client_id, amount, status, payment_date = payable[0]
            output: dict = {
                "payable_id": id,
                "client_id": client_id,
                "amount": float(amount),
                "status": status,
                "payment_date": str(payment_date),
            }
            return success({"message": "Paybles by id", "data": output})

        except Exception as e:
            if isinstance(e, Exception):
                return unprocessable_entity(str(e))
            return server_error("Unexpected Error")
