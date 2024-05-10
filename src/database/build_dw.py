import time
from src.database.base import Base
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class BuildDW(Base):
    def __init__(self):
        super().__init__()

    def create_dw(self):
        time.sleep(5)
        self.connect()
        self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'sales';")
        exists = cursor.fetchone()

        if not exists:
            cursor.execute("CREATE DATABASE sales;")
            cursor = self.conn.cursor()
            cursor.close()
            self.close()
            self.logger.info("Database created.")
            return
        
        self.logger.info("Database already exists.")

    def create_tables(self):
        self.run_file_query(f"{ self.path }/src/query_files/create_dw.sql")

    def build_dw(self):
        self.create_dw()
        self.connect("sales")
        self.create_tables()
        self.close()
        self.logger.info("Data warehouse created.")
