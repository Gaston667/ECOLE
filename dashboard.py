from flask import Blueprint
from flask import Flask, render_template, request, redirect, url_for, session

dashboard_blueprint = Blueprint('dashboard', __name__)

@dashboard_blueprint.route('/dashboard_Profs')
def eleve_dashboard():
    # Code pour récupérer les notes, absences et retards de l'élève depuis la base de données
    # Afficher ces informations dans le modèle HTML
    return  render_template('dashboard_Profs.html', title='dashboard_Profs')
# Espace de gestion des notes pour les enseignants
@dashboard_blueprint.route('/inscription_eleves')
def enseignant_dashboard():
    # Code pour permettre aux enseignants de gérer les notes dans le modèle HTML
    return render_template('inscription_eleves.html', title='dashboard_Profs')
# Page inscription des amin
@dashboard_blueprint.route('/inscription_admin.html')
def direction_dashboard():
    # ....
    return render_template('inscription_admin.html', title='dashboard_Profs')
# Autres routes de tableau de bord si nécessaire


