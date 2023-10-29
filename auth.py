from flask import Blueprint, render_template, request, redirect, url_for, session
from database import DatabaseManager
from werkzeug.security import generate_password_hash, check_password_hash
import dashboard

auth_blueprint = Blueprint('auth', __name__)

# Initialisation de la base de données
db_manager = DatabaseManager('BDD\database.db')

# Connexion à la base de données
curr = db_manager.conn_and_get_cursor()

if db_manager.get_direction_by_params(matricule='EF465') == None:
    db_manager.insert_direction(matricule='EF465', mot_de_passe='12345678', nom='Pruvost', prenom='Marc', email='BLBLBB@gmail.com', telephone='00224897986', poste='Proviseur')
else:
    print('le user existe deja')
    
# Autres routes d'authentification si nécessaire
@auth_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        matricule = request.form['matricule']
        password = request.form['password']
        role = request.form['role']
        if matricule and password and role != '':
            if role == 'direction':
                liste_eleves = db_manager.get_direction_by_params(matricule=matricule,)
                if liste_eleves and check_password_hash(liste_eleves[0]['mot_de_passe'], password):
                    # Utilisateur authentifié, effectuez la redirection en fonction du rôle
                    return "<p>DIRECTION dash</p>"
                else:
                    if not liste_eleves :
                        return render_template('login.html', message = 'Mot de passe incorect') 
                    if liste_eleves['mot_de_passe'] != check_password_hash(liste_eleves['mot_de_passe'], password):
                        return render_template('login.html', message = 'Mot de passe incorect')   
                        
        else:
            return render_template('login.html', message = 'Veuillez remplir tous les champs')
    else:
        return render_template('login.html')

# Autres routes d'authentification si nécessaire
