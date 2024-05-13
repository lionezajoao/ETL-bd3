import os
import psycopg2
from dotenv import load_dotenv
from src.utils import Utils
load_dotenv()

class Base(Utils):
    def __init__(self):
        super().__init__()

    def connect(self, db_name=None):
        try:
            self.conn = psycopg2.connect(
                host=os.environ.get("PG_HOST"),
                database=db_name if db_name else "postgres",
                user=os.environ.get("PG_USER"),
                password=os.environ.get("PG_PASS"),
                port=os.environ.get("PG_PORT")
            )
            self.cur = self.conn.cursor()
            self.logger.info("Connected to database.")
        except Exception as e:
            self.logger.error(f"Error connecting to database, reason: {e}")

    def switch_db(self, db_name):
        try:
            self.cur.execute(f"set search_path to {db_name}")
            self.commit()
            self.logger.info(f"Switched to {db_name} database.")
        except Exception as e:
            self.logger.error(f"Error switching database, reason: {e}")

    def close(self):
        self.cur.close()
        self.conn.close()
        self.logger.info("Connection closed.")

    def create(self, query):
        self.cur.execute(query)
        self.commit()

    def query(self, query, params=None):
        self.logger.info(f"Executing query: {query}")
        self.cur.execute(query, params)
        try:
            return self.cur.fetchall()
        except Exception as e:
            self.logger.error(f"Error fetching data, reason: {e}")
    
    def insert(self, query, params=None):
        try:
            self.cur.execute(query, params)
            self.commit()
            self.logger.debug("Data inserted successfully.")
        except Exception as e:
            self.logger.error(f"Error inserting data, reason: {e}")
            raise e

    def update(self, query, params=None):
        try:
            self.cur.execute(query, params)
            self.commit()
            self.logger.debug("Data updated successfully.")
        except Exception as e:
            self.logger.error(f"Error updating data, reason: {e}")

    def delete(self, query, params=None):
        try:
            self.cur.execute(query, params)
            self.commit()
            self.logger.debug("Data deleted successfully.")
        except Exception as e:
            self.logger.error(f"Error deleting data, reason: {e}")

    def rollback(self):
        self.conn.rollback()

    def commit(self):  
        self.conn.commit()

    def run_file_query(self, file_path):
        with open(file_path, 'r') as file:
            query = file.read()
            self.cur.execute(query)
            self.commit()
            self.logger.debug("Query executed successfully.")
