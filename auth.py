from flask import Blueprint, render_template, request, redirect, url_for
from database import DatabaseManager
from werkzeug.security import generate_password_hash, check_password_hash

auth_blueprint = Blueprint('auth', __name__)

# Initialisation de la base de données
db_manager = DatabaseManager('BDD\database.db')

# Connexion à la base de données
bdd_conn = db_manager.conn
bdd_cursor = db_manager.cursor


# Autres routes d'authentification si nécessaire
@auth_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        matricule = request.form['matricule']
        password = request.form['password']
        role = request.form['role']
        if matricule and password and role != '':
            user = db_manager.get_user_by_matricule(matricule)
            if user and check_password_hash(user['password'], password):
                # Utilisateur authentifié, effectuez la redirection en fonction du rôle
                pass
            else:
                return 'Informations d\'authentification incorrectes'
        else:
            return 'Veuillez remplir tous les champs'
    else:
        return render_template('login.html')

# Autres routes d'authentification si nécessaire
