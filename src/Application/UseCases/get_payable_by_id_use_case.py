from src.Domain.Repository.payable_repository import PayableRepositoryInterface
from src.Application.UseCases.interface_use_case import UseCaseInterface


class GetPayableById(UseCaseInterface):
    def __init__(self, payable_repository: PayableRepositoryInterface) -> None:
        self.__payable_repository = payable_repository

    def execute(self, params):
        try:
            payable = self.__payable_repository.get_payble_id(params["payable_id"])
            if not payable:
                return {"status_code": 404, "body": "Payable not found"}
            id, client_id, amount, status, payment_date = payable[0]
            output = {
                "payable_id": id,
                "client_id": client_id,
                "amount": float(amount),
                "status": status,
                "payment_date": str(payment_date),
            }
            return {"status_code": 200, "body": output}

        except Exception as e:
            if isinstance(e, Exception):
                return {"status_code": 422, "body": str(e)}
            return {"status_code": 500, "body": "Unexpected Error"}
