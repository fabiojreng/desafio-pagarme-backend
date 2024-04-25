import os, sys

sys.path.insert(0, os.path.abspath(os.curdir))

from src.Infra.Http.flask_adapter import FlaskAdapter
from src.Infra.DataBase.connection_mysql import ConnectionMySql
from src.Infra.Repository.MySQL.client_repository_mysql import ClientRepositoryMySQL
from src.Infra.Repository.MySQL.transaction_repository_mysql import (
    TransactionRepositoryMySQL,
)
from src.Infra.Controller.main_controller import MainController
from src.Infra.Repository.MySQL.payable_repository_mysql import PayableRepositoryMySQL
from src.Application.UseCases.create_transaction_use_case import (
    CreateTransactionUseCase,
)
from src.Application.UseCases.create_client_use_case import CreateClientUseCase


server = FlaskAdapter()
connection = ConnectionMySql()
db_transaction = TransactionRepositoryMySQL(connection)
db_client = ClientRepositoryMySQL(connection)
db_payable = PayableRepositoryMySQL(connection)

transaction = CreateTransactionUseCase(db_transaction, db_client, db_payable)
client = CreateClientUseCase(db_client)

MainController(server, transaction, client)
server.listen(3333)
