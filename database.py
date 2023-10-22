import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

class DatabaseManager:
    
    # Initialisation de la base de données
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    # Fonction pour créer les tables de la base de données
    def create_tables(self):
           # Créer la table des élèves
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS eleves (
                                matricule TEXT NOT NULL PRIMARY KEY,
                                mot_de_passe TEXT NOT NULL,
                                nom TEXT NOT NULL,
                                prenom TEXT NOT NULL,
                                age INTEGER,
                                classe_id INTEGER,
                                parent_1_telephone TEXT,
                                parent_2_telephone TEXT,
                                FOREIGN KEY(classe_id) REFERENCES classe(id)
                        )'''
        )
    

        # Créer la table des enseignants
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS enseignants (
                                matricule TEXT NOT NULL PRIMARY KEY,
                                mot_de_passe TEXT NOT NULL,
                                nom TEXT NOT NULL,
                                prenom TEXT NOT NULL,
                                telephone TEXT,
                                email TEXT,
                                materie_id INTEGER,
                                principal_classe_id INTEGER,
                                FOREIGN KEY(principal_classe_id) REFERENCES classe(id)
                                FOREIGN KEY(materie_id) REFERENCES matiere(id)
                                )''')

        # Créer la table du personnel de direction
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS direction (
                                matricule TEXT NOT NULL PRIMARY KEY,
                                mot_de_passe TEXT NOT NULL,
                                nom TEXT NOT NULL,
                                prenom TEXT NOT NULL,
                                email TEXT,
                                telephone TEXT,
                                )''')
        
        # Créer la table des classes
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS classe (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                niveau TEXT NOT NULL,
                                nom TEXT NOT NULL,
                                numero_salle INTEGER NOT NULL
                                )''')
        
        # créer la table Matiere 
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS matiere (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nom TEXT NOT NULL)''')
        
        # Créer la table des notes
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS note (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                eleve_matricule INTEGER,
                                matiere_id INTEGER,
                                note_1 REAL,
                                note_2 REAL,
                                note_3 REAL,
                                trimestre INTEGER,
                                FOREIGN KEY(eleve_matricule) REFERENCES eleves(matricule),
                                FOREIGN KEY(matiere_id) REFERENCES matiere(ID)
                            )''')
        
        # Créer la table des absences
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS absence (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                eleve_matricule INTEGER,
                                date_absence DATE,
                                motif_absence TEXT,
                                FOREIGN KEY(eleve_matricule) REFERENCES eleves(matricule)
                            )''')

        # Enregistrer les modifications
        self.conn.commit()

    # fonction pour insérer un utilisateur dans la base de données
    def insert_eleves(self, matricule, password, nom, prenom, age, classe_id, parent_1_telephone, parent_2_telephone):
        # Code pour insérer un utilisateur dans la base de données
        pass
    
    def insert_enseignants(self, matricule, password, nom, prenom, telephone, email, materie_id, principal_classe_id):
        # Code pour insérer un utilisateur dans la base de données
        pass
    
    def insert_direction(self, matricule, password, nom, prenom, email, telephone):
        # Code pour insérer un utilisateur dans la base de données
        pass

    # Fonction pour récupérer un utilisateur par matricule depuis la base de données
    def get_user_by_matricule(self, matricule):
        # Code pour récupérer un utilisateur par matricule depuis la base de données
        pass

    # Fonction pour fermer la connexion avec la base de données
    def close_connection(self):
        self.conn.close()