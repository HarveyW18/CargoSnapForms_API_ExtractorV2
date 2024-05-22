import os

def get_icon_path():
    # Obtenir le chemin du répertoire actuel
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Recuperer le chemin de l'icone
    icon_path = os.path.join(current_dir, 'icon.ico')

    return icon_path
