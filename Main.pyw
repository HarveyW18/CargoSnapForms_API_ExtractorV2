# Projet/main.py
from Project.Auth import Auth
from Project.App import App
import customtkinter as ctk

def main():
    auth = Auth()
    auth.mainloop()
    if auth.is_authenticated():
        app = App(auth) 
        app.mainloop()
if __name__ == "__main__":
    main()
