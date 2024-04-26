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
        self.__mysql.connect()
        payable = self.__mysql.query("SELECT * FROM payables WHERE id = %s", [id])
        if not payable:
            return None
        self.__mysql.close()
        return payable

    def find_all_payable(self):
        self.__mysql.connect()
        output = self.__mysql.query("SELECT * FROM payables")
        self.__mysql.close()
        return output

    def get_payble_client(self, client_id, status):
        self.__mysql.connect()
        payable = self.__mysql.query(
            "SELECT * FROM payables WHERE client_id = %s AND status = %s",
            [client_id, status],
        )
        if not payable:
            return None
        self.__mysql.close()
        return payable
