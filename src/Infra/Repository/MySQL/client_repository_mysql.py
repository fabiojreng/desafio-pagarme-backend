from src.Domain.Entities.client import Client
from Domain.Repository.client_repository import ClientRepositoryInterface
from src.Infra.DataBase.connection_mysql import ConnectionMySql


class ClientRepositoryMySQL(ClientRepositoryInterface):
    def __init__(self, mysql: ConnectionMySql):
        self.__mysql = mysql

    def save_client(self, client: Client):
        self.__mysql.connect()
        self.__mysql.query(
            "INSERT INTO clients (id, name, email) VALUES (%s, %s, %s)",
            [client["id"], client["name"], client["email"]],
        )
        self.__mysql.close()

    def get_client_id(self, id: str):
        self.__mysql.connect()
        client = self.__mysql.query("SELECT * FROM clients WHERE id = %s", [id])
        self.__mysql.close()
        output = Client.restore(client[0][0], client[0][1], client[0][2]).to_dict()
        return output

    def get_client_email(self, email: str):
        self.__mysql.connect()
        output = self.__mysql.query("SELECT * FROM clients WHERE email = %s", [email])
        self.__mysql.close()
        return output

    def find_all_clients(self):
        pass
