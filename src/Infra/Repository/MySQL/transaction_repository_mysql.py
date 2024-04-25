from src.Domain.Repository.transaction_repository import TransactionRepositoryInterface
from src.Infra.DataBase.connection_mysql import ConnectionMySql
from src.Domain.Entities.transaction import Transaction


class TransactionRepositoryMySQL(TransactionRepositoryInterface):
    def __init__(self, mysql: ConnectionMySql):
        self.__mysql = mysql

    def save_transaction(self, transaction: Transaction):
        self.__mysql.connect()
        self.__mysql.query(
            """INSERT INTO transactions 
                (id, transaction_value, client_id, transaction_description, payment_method, card_number, cardholder_name, card_expiration, cvv) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            [
                transaction["transaction_id"],
                transaction["transaction_value"],
                transaction["client_id"],
                transaction["transaction_description"],
                transaction["payment_method"],
                transaction["card_number"],
                transaction["cardholder_name"],
                transaction["card_expiration"],
                transaction["cvv"],
            ],
        )
        self.__mysql.close()

    def get_transaction_id(self, id: str):
        self.__mysql.connect()
        output = self.__mysql.query("SELECT * FROM transactions WHERE id = %s", [id])
        self.__mysql.close()
        return output

    def find_all_transactions(self):
        pass
