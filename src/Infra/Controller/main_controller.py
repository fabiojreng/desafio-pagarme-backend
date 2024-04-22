from src.Application.UseCases.interface_use_case import UseCaseInterface
from src.Infra.Http.interface_server_http import HttpServer


class MainController:
    def __init__(
        self,
        http_server: HttpServer,
        create_transaction: UseCaseInterface,
        create_paymet: UseCaseInterface,
    ) -> None:
        self.__create_transaction_use_case = create_transaction
        self.__create_payament_use_case = create_paymet
        http_server.register("get", "/", self.__server)
        http_server.register("post", "/transaction", self.__create_transaction)
        http_server.register("post", "/payment", self.__create_payament)

    async def __server(self):
        return {"statusCode": 200, "body": {"message": "Bem Vindo"}}

    async def __create_transaction(self, req):
        output = await self.__create_transaction_use_case.execute(req)
        return output

    async def __create_payament(self, req):
        output = await self.__create_payament_use_case.execute(req)
        return output
