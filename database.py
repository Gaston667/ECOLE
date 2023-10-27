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
                                poste TEXT,
                                )''')
        
        # Créer la table des classes
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS classe (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                niveau TEXT NOT NULL,
                                nom TEXT NOT NULL,
                                numero_salle INTEGER NOT NULL
                                principal_matricule TEXT,
                                FOREIGN KEY(principal_matricule) REFERENCES enseignants(matricule)
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
                                trimestre TEXT,
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
        
        #Crée la table des retards
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS retard (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                eleve_matricule INTEGER,
                                date_retard DATE,
                                motif_retard TEXT,
                                FOREIGN KEY(eleve_matricule) REFERENCES eleves(matricule)
                            )''')

        # Enregistrer les modifications
        self.conn.commit()

    # Fonction pour ajouter un utilisateur(enseignant) dans la base de données
    def insert_enseignant(self, matricule, mot_de_passe, nom, prenom, telephone, email, materie_id):
        self.cursor.execute('''INSERT INTO enseignants (matricule, mot_de_passe, nom, prenom, telephone, email, materie_id) 
                               VALUES (?, ?, ?, ?, ?, ?, ?)''', (matricule, generate_password_hash(mot_de_passe), nom, prenom, telephone, email, materie_id))
        self.conn.commit()

    # Fonction pour ajouter un utilisateur(eleve) dans la base de données
    def insert_direction(self, matricule, mot_de_passe, nom, prenom, email, telephone, poste):
        self.cursor.execute('''INSERT INTO direction (matricule, mot_de_passe, nom, prenom, email, telephone, poste) 
                               VALUES (?, ?, ?, ?, ?, ?, ?)''', (matricule, generate_password_hash(mot_de_passe), nom, prenom, email, telephone, poste))
        self.conn.commit()

    # Fonction pour récupérer un élève par son matricule dans la base de données
    def get_eleve_by_matricule(self, matricule):
        self.cursor.execute("SELECT * FROM eleves WHERE matricule=?", (matricule,))
        eleve = self.cursor.fetchone()
        if eleve:
            return {'user_type': 'eleve', 'matricule': eleve[0], 'mot_de_passe': eleve[1], 'nom': eleve[2], 'prenom': eleve[3], 'age': eleve[4], 'classe_id': eleve[5], 'parent_1_telephone': eleve[6], 'parent_2_telephone': eleve[7]}
        return None

    # Fonction pour récupérer un enseignant par son matricule dans la base de données
    def get_enseignant_by_matricule(self, matricule):
        self.cursor.execute("SELECT * FROM enseignants WHERE matricule=?", (matricule,))
        enseignant = self.cursor.fetchone()
        if enseignant:
            return {'user_type': 'enseignant', 'matricule': enseignant[0], 'mot_de_passe': enseignant[1], 'nom': enseignant[2], 'prenom': enseignant[3], 'telephone': enseignant[4], 'email': enseignant[5], 'materie_id': enseignant[6]}
        return None

    # Fonction pour​ récupérer un directeur par son matricule dans la base de données
    def get_direction_by_matricule(self, matricule):
        self.cursor.execute("SELECT * FROM direction WHERE matricule=?", (matricule,))
        direction_member = self.cursor.fetchone()
        if direction_member:
            return {'user_type': 'direction', 'matricule': direction_member[0], 'mot_de_passe': direction_member[1], 'nom': direction_member[2], 'prenom': direction_member[3], 'email': direction_member[4], 'telephone': direction_member[5], 'poste': direction_member[6]}
        return None
    
    # Fonction pour fermer la connexion avec la base de données
    def close_connection(self):
        self.conn.close()