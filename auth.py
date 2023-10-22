from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

auth_blueprint = Blueprint('auth', __name__)

# Autres routes d'authentification si nécessaire
@auth_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        matricule = request.form['matricule']
        password = request.form['password']
        role = request.form['role']  # Récupérer le rôle depuis le formulaire
        print(matricule, password, role)
        if matricule and password and role != '':
            # Rechercher l'utilisateur dans la base de données
            # Code pour la recherche ici
            # Vérifier les informations d'authentification dans la base de données
            # Code pour la vérification ici
            # Redirection en fonction du rôle (élève, enseignant, direction)
            # Code pour la redirection ici
            # return redirect(url_for('dashboard'))  # Rediriger vers la page appropriée après l'authentification
            pass
        else:
            return 'Veuillez remplir tous les champs'
        
    else:
        return render_template('login.html')

    return render_template('login.html')  # Rediriger vers la page de connexion si la méthode de requête n'est pas POST