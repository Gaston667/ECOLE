from flask import Blueprint
from flask import Flask, render_template, request, redirect, url_for, session

pages_blueprint = Blueprint('pages', __name__)

@pages_blueprint.route('/dashboard_Profs')
# Espace de gestion des notes pour les enseignants
def prof_dashboard():
    # Code pour permettre aux enseignants de gérer les notes dans le modèle HTML
    return  render_template('dashboard_Profs.html', title='dashboard_Profs')

# Espace de Vue des eleves
@pages_blueprint.route('/dashboard_Eleves')
def eleve_dashboard():
    # Code pour permettre aux de voir les notes dans le modèle HTML
    # return render_template('dashboard_Eleves.html', title='Notes-en-ligne')
    return f'<h1>Notes-en-ligne</h1><p>bonjour monsieur</p>'

# Espace de gestion des admins
@pages_blueprint.route('/dashboard_directions')
def direction_dashboard():
    # Code pour permettre aux admins de gérer les notes dans le modèle HTML
    # return render_template('dashboard_Admins.html', title='dashboard_Admins')
    return f'<h1>dashboard_Direction</h1><p>bonjour monsieur</p>'

#Espace d'insciption des profs 
@pages_blueprint.route('/inscription_profs')
def inscription_prof_page():
    # Afficher ces informations dans le modèle HTML
    return render_template('inscription_profs.html', title='Inscription_prof')

#Espace d'insciption des eleves
@pages_blueprint.route('/inscription_eleves')
def inscription_eleve_page():
    # Afficher ces informations dans le modèle HTML
    return render_template('inscription_eleves.html', title='Inscription_élèves')

# Espace d'inscription des admin
@pages_blueprint.route('/inscription_admin.html')
def admin_inscription():
    # Afficher ces informations dans le modèle HTML
    return render_template('inscription_admin.html', title='Inscription_admin')
# Autres routes de tableau de bord si nécessaire


