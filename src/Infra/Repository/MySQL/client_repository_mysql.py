from src.Domain.Entities.client import Client
from src.Domain.Repository.client_repository import ClientRepositoryInterface
from src.Infra.DataBase.connection_mysql import ConnectionMySql


class ClientRepositoryMySQL(ClientRepositoryInterface):
    def __init__(self, mysql: ConnectionMySql):
        self.__mysql = mysql

    def save_client(self, client: Client) -> None:
        self.__mysql.connect()
        self.__mysql.query(
            "INSERT INTO clients (id, name, email) VALUES (%s, %s, %s)",
            [client["id"], client["name"], client["email"]],
        )
        self.__mysql.close()

    def get_client_id(self, id: str) -> Client:
        self.__mysql.connect()
        client = self.__mysql.query("SELECT * FROM clients WHERE id = %s", [id])
        if not client:
            return None
        client_id, client_name, client_email = client[0]
        output = Client.restore(client_id, client_name, client_email).to_dict()
        self.__mysql.close()
        return output

    def get_client_email(self, email: str) -> Client:
        self.__mysql.connect()
        client = self.__mysql.query("SELECT * FROM clients WHERE email = %s", [email])
        client_id, client_name, client_email = client[0]
        output = Client.restore(client_id, client_name, client_email).to_dict()
        self.__mysql.close()
        return output

    def find_all_clients(self) -> list[dict]:
        self.__mysql.connect()
        clients = self.__mysql.query("SELECT * FROM clients")
        self.__mysql.close()
        output = [
            {
                "client_id": client[0],
                "client_name": float(client[1]),
                "client_email": client[2],
            }
            for client in clients
        ]
        return output
