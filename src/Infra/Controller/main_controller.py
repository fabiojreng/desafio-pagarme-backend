from src.Application.UseCases.interface_use_case import UseCaseInterface
from src.Infra.Http.interface_server_http import HttpServer


class MainController:
    def __init__(
        self,
        http_server: HttpServer,
        create_transaction: UseCaseInterface,
        create_client: UseCaseInterface,
    ) -> None:
        self.__create_transaction_use_case = create_transaction
        self.__create_client_use_case = create_client
        http_server.register("get", "/", self.__server)
        http_server.register("post", "/transaction", self.__create_transaction)
        http_server.register("post", "/client", self.__create_client)

    def __server(self):
        return {"statusCode": 200, "body": {"message": "Bem Vindo"}}

    def __create_transaction(self, req):
        output = self.__create_transaction_use_case.execute(req)
        return output

    def __create_client(self, req):
        output = self.__create_client_use_case.execute(req)
        return output
