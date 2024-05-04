from src.Application.UseCases.interface_use_case import UseCaseInterface
from src.Domain.Entities.client import Client
from src.Domain.Repository.client_repository import ClientRepositoryInterface
from src.Domain.Helpers.http_helper import (
    HttpResponse,
    unprocessable_entity,
    success,
    server_error,
)


class CreateClientUseCase(UseCaseInterface):
    def __init__(self, client_repository: ClientRepositoryInterface) -> None:
        self.__client_repository = client_repository

    def execute(self, params: any = None) -> HttpResponse:
        try:
            client_exists = self.__client_repository.get_client_email(params["email"])
            if client_exists:
                return unprocessable_entity("Client already exists")

            client = Client.create(params["name"], params["email"]).to_dict()
            self.__client_repository.save_client(client)
            return success({"message": "Client created successfully", "data": client})
        except Exception as e:
            if isinstance(e, Exception):
                return unprocessable_entity(str(e))
            return server_error("Unexpected Error")
