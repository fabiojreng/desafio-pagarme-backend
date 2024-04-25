from src.Infra.DataBase.connection_mysql import ConnectionMySql
from src.Domain.Repository.payable_repository import PayableRepositoryInterface
from src.Domain.Entities.payable import Payable


class PayableRepositoryMySQL(PayableRepositoryInterface):
    def __init__(self, mysql: ConnectionMySql):
        self.__mysql = mysql

    def save_payable(self, payable: Payable):
        self.__mysql.connect()
        self.__mysql.query(
            "INSERT INTO payables (id, client_id, amount, status, payment_date) VALUES (%s, %s, %s, %s, %s)",
            [
                payable["payment_id"],
                payable["client_id"],
                payable["amount"],
                payable["status"],
                payable["payment_date"],
            ],
        )
        self.__mysql.close()

    def get_payble_id(self, id: str):
        pass

    def find_all_payable(self):
        pass

    def get_payble_client(self, client_id):
        pass
