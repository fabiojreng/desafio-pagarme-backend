import os
from dotenv import load_dotenv
import aiomysql
from src.Infra.DataBase.interface_connection import ConnectionInterface

load_dotenv()


class ConnectionMySql(ConnectionInterface):

    async def connect(self) -> None:
        self.connection = await aiomysql.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            db=os.getenv("DB_NAME"),
        )

    async def query(self, statement: str, params: list = None):
        async with self.connection.cursor() as cursor:
            await cursor.execute(statement, params)
            if statement.strip().split(maxsplit=1)[0].upper() == "SELECT":
                result = await cursor.fetchall()
            else:
                await self.connection.commit()
                result = None
        return result

    async def close(self) -> None:
        await self.connection.close()
