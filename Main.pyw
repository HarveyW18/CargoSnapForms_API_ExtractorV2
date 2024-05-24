import os
import sys
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
from Project.Auth import Auth
from Project.App import App
import customtkinter as ctk

# Chemin du fichier pour stocker la date de première exécution
def get_first_run_file_path():
    # Utilise le répertoire du script ou de l'exécutable
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(application_path, 'Project', 'first.enc')

# Clé de chiffrement générée une seule fois
KEY = b'inWiR-h6TmWAHzGrzqHEFco9d2LaYOqwJ-6nA3bog-k='  # Remplacez ceci par la clé générée

cipher_suite = Fernet(KEY)

def get_first_run_date():
    first_run_file = get_first_run_file_path()
    if not os.path.exists(first_run_file):
        return None
    with open(first_run_file, 'rb') as file:
        encrypted_date = file.read()
        try:
            decrypted_date = cipher_suite.decrypt(encrypted_date).decode('utf-8')
            return datetime.strptime(decrypted_date, '%Y-%m-%d')
        except Exception as e:
            print("Erreur lors du déchiffrement de la date de première exécution :", e)
            return None

def set_first_run_date(date):
    date_str = date.strftime('%Y-%m-%d')
    encrypted_date = cipher_suite.encrypt(date_str.encode('utf-8'))
    first_run_file = get_first_run_file_path()
    with open(first_run_file, 'wb') as file:
        file.write(encrypted_date)

def within_two_months(first_run_date):
    current_date = datetime.now()
    end_date = first_run_date + timedelta(days=60)
    return current_date <= end_date

def main():
    # Vérifiez si c'est la première exécution
    first_run_date = get_first_run_date()
    if first_run_date is None:
        # C'est la première exécution, enregistrez la date
        first_run_date = datetime.now()
        set_first_run_date(first_run_date)

    if within_two_months(first_run_date):
        auth = Auth()
        auth.mainloop()
        if auth.is_authenticated():
            app = App(auth)
            app.mainloop()
    else:
        print("Un problème est survenu. Veuillez contacter le developpeur.")

if __name__ == "__main__":
    main()
