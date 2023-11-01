from flask import Blueprint, render_template, request, redirect, url_for
from database import DatabaseManager
from werkzeug.security import check_password_hash, generate_password_hash

auth_blueprint = Blueprint('auth', __name__)

# Initialisation de la base de données
db_manager = DatabaseManager()
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
            # Vérifie le rôle de l'utilisateur (dans cet exemple, le rôle 'direction')
            if role == 'direction':
                # Utilisation du gestionnaire de contexte 'with' pour assurer une gestion appropriée de la connexion à la base de données
                with db_manager:
                    # Récupère les informations de l'utilisateur (direction) à partir de la base de données
                    directionliste = db_manager.get_direction_by_params(matricule=matricule)
                    # Vérifie si l'utilisateur a été trouvé dans la base de données
                    if directionliste:
                        direction = directionliste[0]
                        # Vérifie le mot de passe hashé
                        print(direction)
                        print(password)
                        if check_password_hash(direction['mot_de_passe'], password) :
                            # Utilisateur authentifié, effectue la redirection vers le tableau de bord de la direction
                            return f"<p>DIRECTION</p><p> bonjour {direction['nom']}</p>"
                        else:
                            # Mot de passe incorrect, affiche un message d'erreur
                            return render_template('login.html', message='Mot de passe incorrect')
                    else:
                        # Utilisateur non trouvé dans la base de données, affiche un message d'erreur
                        return render_template('login.html', message='Utilisateur non trouvé')
        else:
            # Tous les champs ne sont pas remplis, affiche un message d'erreur
            return render_template('login.html', message='Veuillez remplir tous les champs')
    else:
        # Si la requête n'est pas de type POST, affiche la page de formulaire de connexion
        return render_template('login.html', title='Connexion')
