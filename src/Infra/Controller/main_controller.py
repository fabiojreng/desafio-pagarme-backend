from src.Application.UseCases.interface_use_case import UseCaseInterface
from src.Infra.Http.interface_server_http import HttpServer


class MainController:
    def __init__(
        self,
        http_server: HttpServer,
        create_transaction: UseCaseInterface,
        create_client: UseCaseInterface,
        find_all_transactions: UseCaseInterface,
        client_saldo: UseCaseInterface,
        get_payable_id: UseCaseInterface,
    ) -> None:
        self.__create_transaction_use_case = create_transaction
        self.__create_client_use_case = create_client
        self.__find_all_transactions = find_all_transactions
        self.__client_saldo = client_saldo
        self.__get_payable_by_id = get_payable_id
        http_server.register("get", "/", self.__server)
        http_server.register("post", "/create-transaction", self.__create_transaction)
        http_server.register("post", "/create-client", self.__create_client)
        http_server.register("get", "/transactions", self.__transactions)
        http_server.register(
            "get", "/client-amount/<client_id>/<status>", self.__calculate_saldo
        )
        http_server.register("get", "/payable/<payable_id>", self.get_payable_by_id)

    def __server(self):
        return {"status_code": 200, "body": {"message": "Bem Vindo"}}

    def __create_transaction(self, req):
        output = self.__create_transaction_use_case.execute(req)
        return output

    def __create_client(self, req):
        output = self.__create_client_use_case.execute(req)
        return output

    def __transactions(self):
        output = self.__find_all_transactions.execute()
        return output

    def __calculate_saldo(self, req):
        output = self.__client_saldo.execute(req)
        return output

    def get_payable_by_id(self, req):
        output = self.__get_payable_by_id.execute(req)
        return output
