import time
import pandas as pd
from src.database.base import Base
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class BuildDW(Base):
    def __init__(self):
        super().__init__()

    def create_dw(self):
        # time.sleep(2)
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
        self.logger.info("Creating tables.")
        self.run_file_query(f"{ self.path }/src/query_files/create_dw.sql")

    def execute_customers(self):
        self.logger.info("Inserting data into dim_customers table.")
        self.handle_inserts(self.handle_dim_customers(), "dim_customers")
    
    def execute_sales(self):
        self.logger.info("Inserting data into sales table.")
        self.handle_inserts(self.handle_sales(), "sales")

    def execute_products(self):
        self.logger.info("Inserting data into dim_products table.")
        self.handle_inserts(self.handle_dim_products(), "dim_products")

    def execute_dates(self):
        self.logger.info("Inserting data into dim_date table.")
        self.handle_inserts(self.handle_dim_dates(), "dim_date")

    def execute_salesrep(self):
        self.logger.info("Inserting data into dim_salesrep table.")
        self.handle_inserts(self.handle_fact_salesrep(), "dim_salesrep")

    def execute_promotions(self):
        self.logger.info("Inserting data into dim_promotions table.")
        self.handle_inserts(self.handle_promotions(), "dim_promotions")

    def handle_inserts(self, df, table_name):
        columns = ', '.join(df.columns)
        placeholders = ', '.join(['%s' for _ in df.columns])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders}) ON CONFLICT DO NOTHING"

        for index, row in df.iterrows():
            values = row.where(pd.notnull(row), None).tolist()
            self.insert(query, values)

    def build_dw(self):
        # Creating DW db separately to handle different transactions
        self.create_dw()
        self.connect("sales")
        self.create_tables()
        self.execute_customers()
        self.execute_dates()
        self.execute_products()
        self.execute_promotions()
        self.execute_salesrep()
        self.execute_sales()
        self.close()
        self.logger.info("Data warehouse created.")
