from src.Application.UseCases.interface_use_case import UseCaseInterface
from src.Domain.Entities.client import Client
from src.Domain.Repository.client_repository import ClientRepositoryInterface


class CreateClientUseCase(UseCaseInterface):
    def __init__(self, client_repository: ClientRepositoryInterface) -> None:
        self.__client_repository = client_repository

    def execute(self, params):
        try:
            client_exists = self.__client_repository.get_client_email(params["email"])
            if client_exists:
                return {"status_code": 422, "body": "Client already exists"}

            client = Client.create(params["name"], params["email"]).to_dict()
            self.__client_repository.save_client(client)
            return {"status_code": 201, "body": client}
        except Exception as e:
            if isinstance(e, Exception):
                return {"status_code": 422, "body": str(e)}
            return {"status_code": 500, "body": "Unexpected Error"}
