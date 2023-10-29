from flask import Blueprint, render_template, request
from database import DatabaseManager
from werkzeug.security import check_password_hash, generate_password_hash

auth_blueprint = Blueprint('auth', __name__)

# Initialisation de la base de données
<<<<<<< HEAD
db_manager = DatabaseManager('BDD\database.db')

# Connexion à la base de données
bdd_conn = db_manager.conn
bdd_cursor = db_manager.cursor


=======
db_manager = DatabaseManager()
>>>>>>> test
# Autres routes d'authentification si nécessaire
@auth_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    # Vérifie si la requête est de type POST
    if request.method == 'POST':
        # Récupère les données du formulaire
        matricule = request.form['matricule']
        password = request.form['password']
        role = request.form['role']
        # Vérifie si les champs matricule, password et role sont remplis
        if matricule and password and role != '':
            user = db_manager.get_user_by_matricule(matricule)
            if user and check_password_hash(user['password'], password):
                # Utilisateur authentifié, effectuez la redirection en fonction du rôle
                pass
            else:
                return 'Informations d\'authentification incorrectes'
        else:
            # Tous les champs ne sont pas remplis, affiche un message d'erreur
            return render_template('login.html', message='Veuillez remplir tous les champs')
    else:
        # Si la requête n'est pas de type POST, affiche la page de formulaire de connexion
        return render_template('login.html')
