from flask import Blueprint, render_template, request, redirect, url_for
from database import DatabaseManager
from werkzeug.security import check_password_hash

auth_blueprint = Blueprint('auth', __name__)

# Initialisation de la base de données
db_manager = DatabaseManager()

# Autres routes d'authentification si nécessaire
@auth_blueprint.route('/login',  methods=['POST', 'GET'])
def login():
    # Vérifie si la requête est de type POST
    if request.method == 'POST':
        # Récupère les données du formulaire
        matricule = request.form['matricule']
        password = request.form['password']
        role = request.form['role']
        print(matricule, role)
        # Vérifie si les champs matricule, password et role sont remplis
        if matricule and password and role != '':
            # Vérifie le rôle de l'utilisateur (direction ou enseignant ou eleve)
            if role == 'direction':
                # Utilisation du gestionnaire de contexte 'with' pour assurer une gestion appropriée de la connexion à la base de données
                with db_manager:
                    # Récupère les informations de l'utilisateur (direction) à partir de la base de données
                    directionliste = db_manager.get_direction_by_params(matricule=matricule)
                    # Vérifie si l'utilisateur a été trouvé dans la base de données
                    if directionliste:
                        directionMember = directionliste[0]
                        # Vérifie le mot de passe hashé
                        if check_password_hash(directionMember['mot_de_passe'], password) :
                            # Utilisateur authentifié, effectue la redirection vers le tableau de bord de la direction
                            return redirect(url_for('pages.direction_dashboard'))
                        else:
                            # Mot de passe incorrect, affiche un message d'erreur
                            return render_template('login.html', message='Mot de passe incorrect')
                    else:
                        # Utilisateur non trouvé dans la base de données, affiche un message d'erreur
                        return render_template('login.html', message='Utilisateur non trouvé')   
                    
                     
            # Vérifier le role de l'utilisateur (direction ou enseignant ou eleve)
            elif role == 'enseignant':
                # Utilisation du gestionnaire de contexte 'with' pour assurer une gestion appropriée de la connexion à la base de données
                with db_manager:
                    # Récupère les informations de l'utilisateur (enseignant) à partir de la base de données
                    enseignantliste = db_manager.get_enseignant_by_params(matricule=matricule)
                    # Vérifie si l'utilisateur a été trouvé dans la base de données
                    if enseignantliste:
                        enseignant = enseignantliste[0]
                        # Vérifie le mot de passe hashé
                        print(enseignant)
                        print(password)
                        if check_password_hash(enseignant['mot_de_passe'], password) :
                            # Utilisateur authentifié, effectue la redirection vers le tableau de bord de la direction
                            return redirect(url_for('pages.prof_dashboard'))
                        else:
                            # Mot de passe incorrect, affiche un message d'erreur
                            return render_template('login.html', message='Mot de passe incorrect')
                    else:
                        # Utilisateur non trouvé dans la base de données, affiche un message d'erreur
                        return render_template('login.html', message='Utilisateur non trouvé')
                    
                    
            # Vérifier le role de l'utilisateur (direction ou enseignant ou eleve)
            elif role == 'eleve':
                # Utilisation du gestionnaire de contexte 'with' pour assurer une gestion appropriée de la connexion à la base de données
                with db_manager:
                    # Récupère les informations de l'utilisateur (enseignant) à partir de la base de données
                    eleveliste = db_manager.get_eleve_by_params(matricule=matricule)
                    # Vérifie si l'utilisateur a été trouvé dans la base de données
                    if eleveliste:
                        eleve = eleveliste[0]
                        # Vérifie le mot de passe hashé
                        if check_password_hash(eleve['mot_de_passe'], password) :
                            # Utilisateur authentifié, effectue la redirection vers le tableau de bord de la direction
                            return redirect(url_for('pages.eleve_dashboard', eleve_nom=eleve['nom']))
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
    return render_template('login.html', title='Connexion')