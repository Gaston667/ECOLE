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

    # fonction pour ajouter un utilisateur(eleves) dans la base de données
    def insert_eleve(self, matricule, mot_de_passe, nom, prenom, age, classe_id, parent_1_telephone, parent_2_telephone):
        self.cursor.execute('''INSERT INTO eleves (matricule, mot_de_passe, nom, prenom, age, classe_id, parent_1_telephone, parent_2_telephone) 
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                               (matricule, generate_password_hash(mot_de_passe), nom, prenom, age, classe_id, parent_1_telephone, parent_2_telephone))
        self.conn.commit()

    # Fonction pour ajouter un utilisateur(enseignant) dans la base de données
    def insert_enseignant(self, matricule, mot_de_passe, nom, prenom, telephone, email, materie_id):
        self.cursor.execute('''INSERT INTO enseignants (matricule, mot_de_passe, nom, prenom, telephone, email, materie_id) 
                               VALUES (?, ?, ?, ?, ?, ?, ?)''', (matricule, generate_password_hash(mot_de_passe), nom, prenom, telephone, email, materie_id))
        self.conn.commit()

    # Fonction pour ajouter un utilisateur(direction) dans la base de données
    def insert_direction(self, matricule, mot_de_passe, nom, prenom, email, telephone, poste):
        self.cursor.execute('''INSERT INTO direction (matricule, mot_de_passe, nom, prenom, email, telephone, poste) 
                               VALUES (?, ?, ?, ?, ?, ?, ?)''', (matricule, generate_password_hash(mot_de_passe), nom, prenom, email, telephone, poste))
        self.conn.commit()

    # Fonction pour récupérer un élève par son matricule dans la base de données
    def get_eleve_by_params(self, matricule=None, nom=None, prenom=None, classe_id=None):
        query = "SELECT * FROM eleves WHERE"
        params = []

        if matricule:
            query += " matricule=? AND"
            params.append(matricule)
        if nom:
            query += " nom=? AND"
            params.append(nom)
        if prenom:
            query += " prenom=? AND"
            params.append(prenom)
        if classe_id:
            query += " classe_id=? AND"
            params.append(classe_id)

        # Supprime le dernier "AND" de la requête
        query = query[:-4]

        self.cursor.execute(query, tuple(params))
        eleves = self.cursor.fetchall()

        if eleves:
            liste_eleves = []
            for eleve in eleves:
                eleve_info = {
                    'user_type': 'eleve',
                    'matricule': eleve[0],
                    'mot_de_passe': eleve[1],
                    'nom': eleve[2],
                    'prenom': eleve[3],
                    'age': eleve[4],
                    'classe_id': eleve[5],
                    'parent_1_telephone': eleve[6],
                    'parent_2_telephone': eleve[7]
                }
                liste_eleves.append(eleve_info)
            return liste_eleves
        else:
            return print("Aucun élève trouvé avec les critères spécifiés.")

    # Fonction pour récupérer un enseignant par différents critères
    def get_enseignant_by_params(self, matricule=None, nom=None, prenom=None, telephone=None):
        query = "SELECT * FROM enseignants WHERE"
        params = []

        if matricule:
            query += " matricule=? AND"
            params.append(matricule)
        if nom:
            query += " nom=? AND"
            params.append(nom)
        if prenom:
            query += " prenom=? AND"
            params.append(prenom)
        if telephone:
            query += " telephone=? AND"
            params.append(telephone)

        # Supprime le dernier "AND" de la requête
        query = query[:-4]

        self.cursor.execute(query, tuple(params))
        enseignants = self.cursor.fetchall()

        if enseignants:
            liste_enseignants = []
            for enseignant in enseignants:
                enseignant_info = {
                    'user_type': 'enseignant',
                    'matricule': enseignant[0],
                    'mot_de_passe': enseignant[1],
                    'nom': enseignant[2],
                    'prenom': enseignant[3],
                    'telephone': enseignant[4],
                    'email': enseignant[5],
                    'materie_id': enseignant[6]
                }
                liste_enseignants.append(enseignant_info)
            return liste_enseignants
        else:
            return print("Aucun enseignant trouvé avec les critères spécifiés.")

    # Fonction pour récupérer un membre de la direction par différents critères
    def get_direction_by_params(self, matricule=None, nom=None, prenom=None, telephone=None):
        query = "SELECT * FROM direction WHERE"
        params = []

        if matricule:
            query += " matricule=? AND"
            params.append(matricule)
        if nom:
            query += " nom=? AND"
            params.append(nom)
        if prenom:
            query += " prenom=? AND"
            params.append(prenom)
        if telephone:
            query += " telephone=? AND"
            params.append(telephone)

        # Supprime le dernier "AND" de la requête
        query = query[:-4]

        self.cursor.execute(query, tuple(params))
        direction_members = self.cursor.fetchall()

        if direction_members:
            liste_direction = []
            for direction_member in direction_members:
                direction_info = {
                    'user_type': 'direction',
                    'matricule': direction_member[0],
                    'mot_de_passe': direction_member[1],
                    'nom': direction_member[2],
                    'prenom': direction_member[3],
                    'email': direction_member[4],
                    'telephone': direction_member[5],
                    'poste': direction_member[6]
                }
                liste_direction.append(direction_info)
            return liste_direction
        else:
            return print("Aucun membre de la direction trouvé avec les critères spécifiés.")

    # Fonction pour ajouter une classe dans la base de données
    def insert_classe(self, niveau, nom, numero_salle, principal_matricule):
        self.cursor.execute('''INSERT INTO classe (niveau, nom, numero_salle, principal_matricule) 
                           VALUES (?, ?, ?, ?)''', (niveau, nom, numero_salle, principal_matricule))
        self.conn.commit()

    # Fonction pour ajouter une matière dans la base de données
    def insert_matiere(self, nom):
        self.cursor.execute('''INSERT INTO matiere (nom) VALUES (?)''', (nom,))
        self.conn.commit()

    # Fonction pour ajouter une note dans la base de données
    def insert_note(self, eleve_matricule, matiere_id, note_1, note_2, note_3, trimestre):
        self.cursor.execute('''INSERT INTO note (eleve_matricule, matiere_id, note_1, note_2, note_3, trimestre) 
                               VALUES (?, ?, ?, ?, ?, ?)''', (eleve_matricule, matiere_id, note_1, note_2, note_3, trimestre))
        self.conn.commit()

    # Fonction pour ajouter une absence dans la base de données
    def insert_absence(self, eleve_matricule, date_absence, motif_absence):
        self.cursor.execute('''INSERT INTO absence (eleve_matricule, date_absence, motif_absence) 
                               VALUES (?, ?, ?)''', (eleve_matricule, date_absence, motif_absence))
        self.conn.commit()

    # Fonction pour ajouter un retard dans la base de données
    def insert_retard(self, eleve_matricule, date_retard, motif_retard):
        self.cursor.execute('''INSERT INTO retard (eleve_matricule, date_retard, motif_retard) 
                               VALUES (?, ?, ?)''', (eleve_matricule, date_retard, motif_retard))
        self.conn.commit()

    # Fonction pour fermer la connexion avec la base de données
    def close_connection(self):
        self.conn.close()