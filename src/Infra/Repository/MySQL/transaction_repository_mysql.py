from src.Domain.Repository.transaction_repository import TransactionRepositoryInterface
from src.Infra.DataBase.connection_mysql import ConnectionMySql
from src.Domain.Entities.transaction import Transaction


class TransactionRepositoryMySQL(TransactionRepositoryInterface):
    def __init__(self, mysql: ConnectionMySql):
        self.__mysql = mysql

    def save_transaction(self, transaction: Transaction) -> None:
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

    def get_transaction_id(self, id: str) -> list:
        self.__mysql.connect()
        transaction = self.__mysql.query(
            "SELECT * FROM transactions WHERE id = %s", [id]
        )
        self.__mysql.close()
        return transaction

    def find_all_transactions(self) -> list[dict]:
        self.__mysql.connect()
        transactions = self.__mysql.query("SELECT * FROM transactions")
        self.__mysql.close()
        output = [
            {
                "transaction_id": transaction[0],
                "transaction_value": float(transaction[1]),
                "client_id": transaction[2],
                "transaction_description": transaction[3],
                "payment_method": transaction[4],
                "card_number": transaction[5],
                "cardholder_name": transaction[6],
                "card_expiration": transaction[7],
                "cvv": transaction[8],
            }
            for transaction in transactions
        ]
        return output
