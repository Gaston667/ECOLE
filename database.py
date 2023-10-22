import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        # Code pour créer les tables dans la base de données
        pass

    def insert_user(self, matricule, password, role):
        # Code pour insérer un utilisateur dans la base de données
        pass

    def get_user_by_matricule(self, matricule):
        # Code pour récupérer un utilisateur par matricule depuis la base de données
        pass

    def close_connection(self):
        self.conn.close()