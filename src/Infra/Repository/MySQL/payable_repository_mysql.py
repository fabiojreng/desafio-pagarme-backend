from src.Infra.DataBase.connection_mysql import ConnectionMySql
from src.Domain.Repository.payable_repository import PayableRepositoryInterface
from src.Domain.Entities.payable import Payable


class PayableRepositoryMySQL(PayableRepositoryInterface):
    def __init__(self, mysql: ConnectionMySql):
        self.__mysql = mysql

    def save_payable(self, payable: Payable) -> None:
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

    def get_payble_id(self, id: str) -> dict:
        self.__mysql.connect()
        payable = self.__mysql.query("SELECT * FROM payables WHERE id = %s", [id])
        if not payable:
            return None
        id_, id_client, amount, payable_status, payment_date = payable[0]
        output = {
            "payable_id": id_,
            "client_id": id_client,
            "amount": float(amount),
            "status": payable_status,
            "payment_date": payment_date,
        }
        self.__mysql.close()
        return output

    def find_all_payable(self) -> list[dict]:
        self.__mysql.connect()
        payables = self.__mysql.query("SELECT * FROM payables")
        self.__mysql.close()
        output = [
            {
                "payable_id": payable[0],
                "client_id": payable[1],
                "client_id": payable[2],
                "amount": payable[3],
                "status": payable[4],
                "payment_date": payable[5],
            }
            for payable in payables
        ]
        return output

    def get_paybles_client(self, client_id, status) -> list[dict]:
        self.__mysql.connect()
        payables = self.__mysql.query(
            "SELECT * FROM payables WHERE client_id = %s AND status = %s",
            [client_id, status],
        )
        if not payables:
            return None
        self.__mysql.close()
        output = [
            {
                "payable_id": payable[0],
                "client_id": payable[1],
                "amount": float(payable[2]),
                "status": payable[3],
                "payment_date": str(payable[4]),
            }
            for payable in payables
        ]
        return output
