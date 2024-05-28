from datetime import datetime, timedelta
import requests
import csv
import re
import os

class CargoSnapModel:
    def __init__(self):
        pass

    def authenticate(self, token):
        url = "https://api.cargosnap.com/api/v2/forms/3627"

        params = {
            "format": "json",
            "token": token
        }
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            return "Authentification réussie"
        elif response.status_code == 401:
            return "Authentification échouée: Token invalide"
        elif response.status_code == 403:
            return "Authentification échouée: Vous n'avez pas le droit d'accéder à cette ressource"
        elif response.status_code == 404:
            return "Authentification échouée: Ressource non trouvée"
        else:
            return f"Erreur {response.status_code} : Veuillez contacter l'administrateur C.Wonga"
        


    def iso_week_to_date(self, iso_week):
    # Obtenir l'année actuelle
        current_year = datetime.today().year

        # Calculer la date du lundi correspondant à la semaine ISO spécifiée
        # Nous utilisons le lundi de la semaine ISO spécifiée comme point de départ
        start_date = datetime.strptime(f"{current_year}-W{iso_week}-1", "%Y-W%W-%w")

        # Trouver le dimanche de la semaine précédente
        end_date = start_date + timedelta(days=6)

        # Convertir les dates en format ISO 8601 (YYYY-MM-DD)
        start_date_str = start_date.strftime("%Y-%m-%d")
        end_date_str = end_date.strftime("%Y-%m-%d")

        return start_date_str, end_date_str
    
    
    def fetch_data_date(self, start_date_str, end_date_str, token):

        url = "https://api.cargosnap.com/api/v2/forms/3627"
        url2 = "https://api.cargosnap.com/api/v2/forms/4247"

        params = {
            "format": "json",
            "token": token,
            "startdate": start_date_str,
            "enddate": end_date_str,
            "limit": 250
        }
        response = requests.get(url, params=params)
        response2 = requests.get(url2, params=params)

        if response.status_code and response2.status_code == 200:
            data = response.json()
            data2 = response2.json()
            return data, data2
        else:
            return None

    def fetch_data_week(self, iso_week, token):
        # Utiliser la fonction iso_week_to_date pour obtenir les dates de début et de fin
        start_date_str, end_date_str = self.iso_week_to_date(iso_week)

        url = "https://api.cargosnap.com/api/v2/forms/3627"
        url2 = "https://api.cargosnap.com/api/v2/forms/4247"

        params = {
            "format": "json",
            "token": token,
            "startdate": start_date_str,
            "enddate": end_date_str,
            "limit": 250
        }
        response = requests.get(url, params=params)
        response2 = requests.get(url2, params=params)
        
        if response.status_code == 200 and response2.status_code == 200:
            data = response.json()
            data2 = response2.json()
            return data, data2
        else:
            return None
        

    def export_to_csv(self, data, data2, file_name):
        if data and "data" in data and data2 and "data" in data2:
            # Créer le répertoire ExportCSV s'il n'existe pas déjà
            export_dir = "ExportCSV"
            os.makedirs(export_dir, exist_ok=True)

            file_path = os.path.join(export_dir, file_name + ".csv")
            with open(file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
                fieldnames = ["BR", "Quality mark", "Potential of storage", "Sum Up", "Sorting", "Relabelling", "Repalettizing", "Resizing", "Rejection"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
                writer.writeheader()

                for item in data["data"]:
                    row_data = {key: '' for key in fieldnames}
                    # Utiliser une expression régulière pour rechercher les 5 chiffres après "BR" dans le scan_code
                    match = re.search(r'BR(\d{5})', item.get("scan_code", ""))
                    # Si une correspondance est trouvée, ajouter la ligne au fichier de sortie
                    if match:
                        row_data["BR"] = match.group(1)
                        # Récupérer les champs "BR", "Quality mark", "Potential of storage" et "Sum Up" depuis item
                        for form_field in item.get("form", {}).get("fields", []):
                            field_label = form_field.get("label", "").strip()
                            field_value = form_field.get("value", "").replace("\n", " ")
                            if field_label in row_data:
                                row_data[field_label] = field_value

                        # Liste des champs à vérifier
                    fields_to_check = ["Sorting", "Relabelling", "Repalettizing", "Resizing", "Rejection"]

                    # Trouver l'élément correspondant dans data2 en fonction du scan_code
                    corresponding_item2 = next((item2 for item2 in data2["data"] if item2.get("scan_code") == item.get("scan_code")), None)

                    if corresponding_item2:
                        form_fields = {field.get("label", "").strip(): field.get("value", "").replace("\n", " ") for field in corresponding_item2.get("form", {}).get("fields", [])}
                        for field_label in fields_to_check:
                            row_data[field_label] = form_fields.get(field_label, "no")
                    else:
                        # Si aucun élément correspondant n'est trouvé dans data2, attribuer "No" aux champs restants de row_data
                        for field_label in fields_to_check:
                            row_data[field_label] = "no"

                    writer.writerow(row_data)

            return "Données exportées avec succès dans le fichier CSV."
        else:
            return "Aucune donnée trouvée dans la réponse."