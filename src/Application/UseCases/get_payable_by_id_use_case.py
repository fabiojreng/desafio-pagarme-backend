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

            return success({"message": "Paybles by id", "data": payable})

        except Exception as e:
            if isinstance(e, Exception):
                return unprocessable_entity(str(e))
            return server_error("Unexpected Error")
