from .CargoSnapModel import CargoSnapModel
from .Assets.Icon.iconpath_config import get_icon_path
import tkinter as tk
import customtkinter as ctk

class Auth(ctk.CTk):
    def __init__(self, root=None):
        super().__init__(root)
        self.bg = self.cget("fg_color")
        self.num_of_frames = 0
        self.title("GHELFER - CargoSnap")
        self.iconbitmap(get_icon_path())
        
        # Obtenir la largeur et la hauteur de l'écran
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Définir la largeur et la hauteur de la fenêtre
        window_width = 500
        window_height = 200

        # Empêcher le redimensionnement de la fenêtre
        self.resizable(False, False)

        # Calculer la position de la fenêtre pour la centrer
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Positionner la fenêtre au centre de l'écran
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        # Déclaration d'une variable pour suivre l'état d'authentification
        self.authenticated = False

        # root!
        main_container = ctk.CTkFrame(self, corner_radius=8, fg_color=self.bg)
        main_container.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        # Variable pour stocker le token
        self.token = None  # Variable pour stocker le token
        # Ajouter les widgets au conteneur principal
        self.token_label("Veuillez entrer le token d'authentification CargoSnap", main_container)
        self.token_entry_widget = self.token_entry(main_container)  # Stocker le widget Entry dans une variable d'instance
        self.token_button("Valider", self.token_button_action, main_container)

        # Créer le label pour afficher les messages d'authentification
        self.label_auth_result = ctk.CTkLabel(main_container, corner_radius=8, fg_color=self.bg)
        self.label_auth_result.pack(fill=tk.X, padx=8, pady=8)
        self.label_auth_result.configure(text=" ")

    def token_label(self, text, container):
        label = ctk.CTkLabel(container, text=text, corner_radius=8, fg_color=self.bg, font=("Segoe UI", 14))
        label.pack(fill=tk.X, padx=8, pady=8)
        return label

    def token_entry(self, container):
        entry = ctk.CTkEntry(container, corner_radius=8, fg_color=self.bg, width=12, height=30, border_width=1, border_color='#476A4A', placeholder_text="Token d'authentification")
        entry.pack(fill=tk.X, padx=100, pady=8)
        return entry

    def token_button(self, text, command, container):
        button = ctk.CTkButton(container, text=text, corner_radius=8, fg_color='#476A4A', command=command, font=("Segoe UI", 12, "bold"))
        button.pack(fill=tk.X, padx=200, pady=8)
        return button
    
    def clear_message(self):
        self.label_auth_result.configure(text="")

    def is_authenticated(self):
        return self.authenticated
    
    def get_token(self):
        return self.token
    
    def token_button_action(self):
        # Récupérer le token entré par l'utilisateur
        self.token = self.token_entry_widget.get()

        data = CargoSnapModel()

        # Appeler la méthode authenticate avec le token
        message = data.authenticate(self.token)

        if message == "Authentification réussie":
            # Afficher un message d'authentification réussie
            self.label_auth_result.configure(text=message, text_color="green", font=("Segoe UI", 13, "bold"))
            after_id = self.after(1500, self.destroy)
            # Mettre à jour l'état d'authentification
            self.authenticated = True
        else:
            # Afficher un message d'authentification échouée
            self.label_auth_result.configure(text=message, text_color="red", font=("Segoe UI", 13, "bold"))
            self.label_auth_result.after(1900, self.clear_message)  # Efface le message après 2 secondes
