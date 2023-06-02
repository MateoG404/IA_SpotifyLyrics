
# Librerias

from dependences import instalar_dependencias
from api_spotify import __init__
import os
import pkg_resources

# Obtener ruta de archivo 
def get_PATH_URL():
    carpeta_padre = os.path.dirname(os.getcwd())
    # Retorna dirección URLS_Spotify completa
    return os.path.join(carpeta_padre, 'Data', 'URLS_Spotify.txt') 

# Instalación de dependencias

instalar_dependencias()

# Obtener datos de Spotify de los albums

if not os.path.exists(get_PATH_URL()):
    print("WE")
    # Crear archivo dataFrame_albums con  la información de los albums
    __init__()

# Obtener datos de 
#if not os.patnot os.path.exists(get_PATH_URL())