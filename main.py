from src.database.base import Database

if __name__ == "__main__":
    db = Database()
    db.connect()
    db.run_file_query(f"{ db.path }/src/query_files/create_dw.sql")