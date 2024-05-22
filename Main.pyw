# Projet/main.py
from Project.Auth import Auth
from Project.App import App
import customtkinter as ctk

def main():
    # Instanciez la classe d'authentification une seule fois en dehors de la condition
    auth = Auth()
    auth.mainloop()

    # Une fois l'authentification réussie, instanciez et exécutez l'application principale
    if auth.is_authenticated():
        app = App(auth)  # Passez l'instance auth à App
        app.mainloop()

if __name__ == "__main__":
    main()
