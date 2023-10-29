from flask import Flask, render_template, request, redirect, url_for, session
from auth import auth_blueprint
from dashboard import dashboard_blueprint
from database import DatabaseManager

app = Flask(__name__)   
app.secret_key = "A!a1V@2h83*)}{"

# Initialisation de la base de données
db_manager = DatabaseManager()


# Enregistrement des Blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(dashboard_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
