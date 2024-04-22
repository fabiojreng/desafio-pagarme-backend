import os, sys

sys.path.insert(0, os.path.abspath(os.curdir))
from src.Infra.DataBase.connection_mysql import ConnectionMySql
from src.Infra.Repository.repository_mysql import RepositoryMySQL
from src.Application.UseCases.create_payable_use_case import CreatePayableUseCase
from src.Application.UseCases.create_transaction_use_case import (
    CreateTransactionUseCase,
)
from src.Infra.Controller.main_controller import MainController
from src.Infra.Http.flask_adapter import FlaskAdapter


server = FlaskAdapter()
connection = ConnectionMySql()
db = RepositoryMySQL(connection)
transaction = CreateTransactionUseCase(db)
payable = CreatePayableUseCase(db)
MainController(server, transaction, payable)
server.listen(3333)
