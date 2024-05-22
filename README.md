---

# GHELFER - CargoSnap Extracteur CSV
Ce projet consiste en une application GUI permettant d'extraire des données à partir de l'API CargoSnap et de les exporter vers un fichier CSV. L'application permet à l'utilisateur d'entrer des paramètres tels que les dates, la semaine ISO et le nom du fichier CSV, et utilise l'authentification via token pour accéder aux données de CargoSnap.

## Fonctionnalités
- **Interface Utilisateur conviviale :** Une interface graphique simple et conviviale permet à l'utilisateur d'interagir facilement avec l'application.
- **Authentification sécurisée :** L'application utilise un token d'authentification pour garantir l'accès sécurisé aux données de CargoSnap.
- **Extraction de données :** Les données sont extraites de l'API CargoSnap en fonction des paramètres spécifiés par l'utilisateur.
- **Exportation vers CSV :** Les données extraites sont exportées vers un fichier CSV pour une utilisation ultérieure ou une analyse.

## Prérequis
- Python 3.x
- tkinter (installé par défaut avec Python)
- customtkinter
- re
- tkcalendar
- requests

## Installation
1. Clonez ce dépôt vers votre machine locale :
```
git clone https://github.com/HarveyW18/GHELFER-CargoSnap.git
```
2. Installez les dépendances nécessaires :
Pour pouvoir installer les dépendances nécessaires, vous devez aller dans le repertoire principal et executer la commander suivante :
```
pip install .
```

## Utilisation
1. Exécutez le fichier `main.py` pour lancer l'application.
2. Entrez votre token d'authentification CargoSnap dans le champ prévu à cet effet.
3. Entrez les dates ou la semaine ISO, ainsi que le nom du fichier CSV dans les champs correspondants.
4. Sélectionnez les options souhaitées.
5. Cliquez sur le bouton "Extraire" pour récupérer et exporter les données vers le fichier CSV.

## Auteur
- HarveyW18

## Licence
Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

--- 

Assurez-vous de personnaliser les sections selon les spécificités de votre projet. Si vous avez d'autres fonctionnalités ou détails à ajouter, n'hésitez pas à les inclure.

-----------------------------------------------------------------------------------------------------

# Project Title: CargoSnap Extractor

## Description:
This project is a Python application designed to extract data from CargoSnap API and export it to a CSV file. It provides a graphical user interface (GUI) built using the Tkinter library for user interaction.

## Features:
- Authentication with CargoSnap API using a token.
- Extraction of data based on specified date range or ISO week.
- Export extracted data to a CSV file.
- User-friendly GUI for ease of use.

## Installation:
1. Clone the repository:
   ```
   git clone https://github.com/HarveyW18/CargoSnapExtractor.git
   ```
2. Navigate to the project directory:
   ```
   cd CargoSnapExtractor
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage:
1. Run the `main.py` file:
   ```
   python main.py
   ```
2. Enter your CargoSnap authentication token and click "Valider".
3. Fill in the required fields:
   - Enter start and end dates OR ISO week.
   - Provide a filename for the CSV export.
   - Choose between "Semaine ISO" or "Date" options.
4. Click "Extraire" to extract data.

## Dependencies:
- `requests`: For making HTTP requests to the CargoSnap API.
- `tkinter`: For building the graphical user interface.
- `tkcalendar`: For the date entry widget in the GUI.
- `customtkinter`
- `re`

## Structure:
- `main.py`: Main entry point of the application.
- `CargoSnapModel.py`: Module containing the CargoSnapModel class for data extraction and CSV export.
- `Auth.py`: Module for CargoSnap authentication.
- `customtkinter.py`: Module containing custom Tkinter widgets for styling the GUI.

## Contributors:
- HarveyW18

## License:
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
