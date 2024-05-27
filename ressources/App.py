from .CargoSnapModel import CargoSnapModel
from .Assets.Icon.iconpath_config import get_icon_path
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import customtkinter as ctk
import re

class App(ctk.CTk):
    def __init__(self, auth_instance, root=None):
        super().__init__(root)
        self.auth_instance = auth_instance
        self.bg = self.cget("fg_color")
        self.title("GHELFER - CargoSnap")
        self.iconbitmap(get_icon_path())
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = 400
        window_height = 600
        min_window_width = 400
        min_window_height = 600
        max_window_width = 400
        max_window_height = 600
        self.minsize(min_window_width, min_window_height)
        self.maxsize(max_window_width, max_window_height)

        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        self.main_container = ctk.CTkFrame(self, corner_radius=8, fg_color=self.bg)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        self.title_text("Extracteur de CargoSnap CSV", self.main_container)
        self.date_label("", self.main_container)
        self.date_label("Veuillez entrer les dates (AAAA-MM-JJ)", self.main_container)
        self.date_entry_fields(self.main_container)
        self.isoweek_label("Veuillez entrer la semaine ISO", self.main_container)
        self.isoweek_entry(self.main_container)
        self.filename_label("Veuillez entrer le nom du fichier", self.main_container)
        self.filename_entry(self.main_container)
        self.option_choice_text("Options", self.main_container)
        self.create_radio_buttons(self.main_container)
        self.date_label("", self.main_container)
        self.submit_button(self.main_container)
        self.message_label = ctk.CTkLabel(self.main_container, corner_radius=8, fg_color=self.bg)
        self.message_label.pack(fill=tk.X, padx=8, pady=8)
        self.message_label.configure(text="")

    def title_text(self, text, container):
        label = ctk.CTkLabel(container, text=text, corner_radius=8, fg_color=self.bg, font=("Segoe UI", 15, "bold"))
        label.pack(fill=tk.X, padx=8, pady=8)
        return label
    
    def date_label(self, text, container):
        label = ctk.CTkLabel(container, text=text, corner_radius=8, fg_color=self.bg, font=("Segoe UI", 14))
        label.pack(fill=tk.X, padx=8, pady=8)
        return label
    
    def validate_date(self, P):
    #Valide si la chaîne de caractères est une date au format AAAA-MM-JJ."""
        if P == "" or re.fullmatch(r'(\d{0,4}(-\d{0,2}(-\d{0,2})?)?)?', P):
            if len(P) >= 7 and P[6] != '-':  # Si la chaîne de caractères est assez longue pour contenir un mois
                month = int(P[5:7])
                if month < 1 or month > 12:
                    return False
            if len(P) == 10 and P[9] != '-':  # Si la chaîne de caractères est assez longue pour contenir un jour
                day = int(P[8:10])
                if day < 1 or day > 31:
                    return False
            return True
        return False
    
        
    def date_entry_fields(self, container):
        frame = ctk.CTkFrame(container, fg_color=self.bg)
        frame.pack(pady=8)

        def get_monday():
            current_date = datetime.today()
            current_iso_week = current_date.isocalendar()[1]
            monday = datetime.strptime(f"{current_date.year}-W{current_iso_week}-1", "%Y-W%W-%w")
            return monday.strftime("%Y-%m-%d")

        self.start_date_entry = DateEntry(frame, width=12, background="#242424", foreground='white', borderwidth=1, bordercolor="#476A4A", date_pattern='yyyy-mm-dd')
        self.start_date_entry.set_date(get_monday())
        self.start_date_entry.configure(headersbackground="#242424", headersforeground='white', selectbackground="#476A4A", selectforeground='white', normalbackground="#242424", normalforeground='white', weekendbackground="#242424", weekendforeground='white')
        self.start_date_entry.grid(row=0, column=0, padx=5)

        to_label = ctk.CTkLabel(frame, text="au", corner_radius=8, fg_color=self.bg, font=("Segoe UI", 13))
        to_label.grid(row=0, column=1, padx=5)

        def get_sunday():
            monday = datetime.strptime(get_monday(), "%Y-%m-%d")
            sunday = monday + timedelta(days=6)
            return sunday.strftime("%Y-%m-%d")

        self.end_date_entry = DateEntry(frame, width=12, background="#242424", foreground='white', borderwidth=1, bordercolor="#476A4A", date_pattern='yyyy-mm-dd')
        self.end_date_entry.set_date(get_sunday())
        self.end_date_entry.configure(headersbackground="#242424", headersforeground='white', selectbackground="#476A4A", selectforeground='white', normalbackground="#242424", normalforeground='white', weekendbackground="#242424", weekendforeground='white')
        self.end_date_entry.grid(row=0, column=2, padx=5)
    
    def isoweek_label(self, text, container):
        label = ctk.CTkLabel(container, text=text, corner_radius=8, fg_color=self.bg, font=("Segoe UI", 14))
        label.pack(fill=tk.X, padx=8, pady=8)
        return label
    
    def current_iso_week(self):
        return datetime.today().isocalendar()[1]
    
    def isoweek_entry(self, container):
        def validate_input(text):
            if text.isdigit() and len(text) <= 2 and 1 <= int(text) <= 53:
                return True
            elif text == "" or text == "\x08":  # Vérifie si la touche pressée est la touche de suppression
                return True
            else:
                return False

        vcmd = (self.register(validate_input), '%P')
    
        self.isoweek_entry = ctk.CTkEntry(container, corner_radius=8, fg_color=self.bg, width=12, height=30, border_width=1, border_color='#476A4A', placeholder_text=str(self.current_iso_week()), validate='key', validatecommand=vcmd)
        self.isoweek_entry.pack(fill=tk.X, padx=100, pady=8)
        return self.isoweek_entry
    
    def filename_label(self, text, container):
        label = ctk.CTkLabel(container, text=text, corner_radius=8, fg_color=self.bg, font=("Segoe UI", 14))
        label.pack(fill=tk.X, padx=8, pady=8)
        return label
    
    def filename_entry(self, container):
        self.filename_entry = ctk.CTkEntry(container, corner_radius=8, fg_color=self.bg, width=12, height=30, border_width=1, border_color='#476A4A', placeholder_text=f"Cargo_S{self.current_iso_week()}")
        self.filename_entry.pack(fill=tk.X, padx=100, pady=8)
        return self.filename_entry
    
    def option_choice_text(self, text, container):
        label = ctk.CTkLabel(container, text=text, corner_radius=8, fg_color=self.bg, font=("Segoe UI", 14))
        label.pack(fill=tk.X, padx=8, pady=8)
        return label
    
    def create_radio_buttons(self, container):
        radio_frame = ctk.CTkFrame(container, fg_color=self.bg)
        radio_frame.pack(fill=tk.X, padx=8, pady=8)

        # Variable pour stocker le choix de l'option
        self.option_choice = tk.StringVar()

        # Fonction pour gérer le choix de l'option
        def option_selected():
            choice = self.option_choice.get()
            if choice == "Semaine ISO":
                # Désactiver les champs de saisie de date
                self.start_date_entry.configure(state=tk.DISABLED)
                self.end_date_entry.configure(state=tk.DISABLED)
                # Activer l'entrée de la semaine ISO
                self.isoweek_entry.configure(state=tk.NORMAL)
            elif choice == "Date":
                # Désactiver l'entrée de la semaine ISO
                self.isoweek_entry.configure(state=tk.DISABLED)
                # Activer les champs de saisie de date
                self.start_date_entry.configure(state=tk.NORMAL)
                self.end_date_entry.configure(state=tk.NORMAL)

        # Créer les boutons radio
        style = ttk.Style()
        # Style des boutons radio
        style.configure("Red.TRadiobutton", 
                        background="#242424", 
                        foreground="#FFFFFF", 
                        anchor="center", 
                        font=("Segoe UI", 9),  # Ajoute une police d'écriture
                        indicatorcolor="#242424", 
                        indicatordiameter=10, 
                        indicatorrelief=tk.FLAT,
                        highlightthickness=0)

        radio_sem_iso = ttk.Radiobutton(radio_frame, text="Semaine ISO", variable=self.option_choice, value="Semaine ISO", command=option_selected, style="Red.TRadiobutton")
        radio_sem_iso.pack(side=tk.LEFT, anchor='center', padx=(90, 20))
        radio_date = ttk.Radiobutton(radio_frame, text="Date", variable=self.option_choice, value="Date", command=option_selected, style="Red.TRadiobutton")
        radio_date.pack(side=tk.LEFT, anchor='center', padx=(25, 0))
        # Choisir l'option par défaut comme Semaine ISO
        self.option_choice.set("Semaine ISO")

    def submit_button(self, container):
        button = ctk.CTkButton(container, text="Extraire", corner_radius=8, fg_color="#476A4A", command=self.use_entry_values, font=("Segoe UI", 13, "bold"))
        button.pack(fill=tk.X, padx=8, pady=8)
        return button

    def get_token(self):
        # Récupérer le token de l'instance de Auth
        token = self.auth_instance.get_token()
        return token
    
    def get_iso_week(self):
        isoweek_str = self.isoweek_entry.get().strip()
        return isoweek_str
    
    def get_date_range(self):
        start_date_str = self.start_date_entry.get_date().strftime('%Y-%m-%d')
        end_date_str = self.end_date_entry.get_date().strftime('%Y-%m-%d')
        return start_date_str, end_date_str

    def use_entry_values(self):
        # Récupérer les valeurs des champs de saisie
        start_date_str = self.start_date_entry.get_date().strftime('%Y-%m-%d')
        end_date_str = self.end_date_entry.get_date().strftime('%Y-%m-%d')
        isoweek_str = self.isoweek_entry.get().strip()
        filename_str = self.filename_entry.get() + f"_{datetime.now().year}_S{isoweek_str if self.option_choice.get() == 'Semaine ISO' else ''}".strip()

        # Récupérer le token à partir de l'instance de Auth
        token = self.auth_instance.get_token()

        # Instancier le modèle CargoSnap
        cargo_model = CargoSnapModel()

        # Vérifier l'option choisie et valider les entrées correspondantes
        option = self.option_choice.get()
        if option == "Semaine ISO":
            if not isoweek_str:
                self.show_message("Veuillez entrer une semaine ISO.", "red")
                return
            # Vérifier si le nom de fichier est vide
            if not filename_str:
                self.show_message("Veuillez entrer un nom valide pour le fichier.", "red")
                return
            data, data2 = cargo_model.fetch_data_week(isoweek_str, token)
        elif option == "Date":
            if not start_date_str or not end_date_str:
                self.show_message("Veuillez entrer les dates de début et de fin.", "red")
                return
            elif start_date_str > end_date_str:
                self.show_message("La date de début doit être antérieure à la date de fin.", "red")
                return
            data, data2 = cargo_model.fetch_data_date(start_date_str, end_date_str, token)
        else:
            self.show_message("Veuillez choisir une option entre Semaine ISO et Date.", "red")
            return
        
        # Vérifier si le nom de fichier est vide
        if not filename_str:
            self.show_message("Veuillez entrer un nom valide pour le fichier.", "red")
            return

        # Vérifier si des données ont été récupérées
        if data:
            export = cargo_model.export_to_csv(data, data2, filename_str)
            if export == "Données exportées avec succès dans le fichier CSV.":
                self.show_message("Données exportées avec succès.", "green")
            else:
                self.show_message("Échec de l'export des données.", "red")
        else:
            self.show_message("Aucune donnée trouvée dans la réponse.", "red")

    def show_message(self, message, color):
        """Affiche un message coloré dans le label message_label."""
        self.message_label.configure(text=message, text_color=color, font=("Segoe UI", 13, "bold"))
        self.message_label.after(2000, self.clear_message)

    def clear_message(self):
        """Efface le message affiché dans le label message_label."""
        self.message_label.configure(text="")

