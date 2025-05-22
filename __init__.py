from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #Comm2

@app.route('/encrypt/<key>/<valeur>')
def encryptage(key, valeur):
    try:
        f = Fernet(key.encode())  # Crée un objet Fernet avec la clé fournie
        valeur_bytes = valeur.encode()
        token = f.encrypt(valeur_bytes)
        return f"Valeur encryptée : {token.decode()}"
    except Exception as e:
        return f"Erreur dans l'encryptage : {str(e)}"

@app.route('/decrypt/<key>/<valeur>')
def decryptage(key, valeur):
    try:
        f = Fernet(key.encode())
        valeur_bytes = valeur.encode()
        original = f.decrypt(valeur_bytes)
        return f"Valeur déchiffrée : {original.decode()}"
    except InvalidToken:
        return "Clé invalide ou token corrompu."
    except Exception as e:
        return f"Erreur dans le déchiffrement : {str(e)}"

@app.route('/generate-key')
def generate_key():
    return f"Voici votre clé personnelle : {Fernet.generate_key().decode()}"

if name == "main":
    app.run(debug=True)
