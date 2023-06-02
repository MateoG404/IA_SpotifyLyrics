
# Librerias

from dependences import instalar_dependencias
from api_spotify import __init__
from songs import __init_songs__
import os
import pkg_resources

# Obtener ruta de archivo 
def get_PATH_URL():
    carpeta_padre = os.path.dirname(os.getcwd())
    # Retorna dirección URLS_Spotify completa
    return carpeta_padre

# Instalación de dependencias

instalar_dependencias()

carpeta_padre = get_PATH_URL()

# Obtener datos de Spotify de los albums
if not os.path.exists(os.path.join(carpeta_padre, 'Data', 'dataframe_albums.pkl') ):
    # Crear archivo dataFrame_albums con  la información de los albums
    __init__()

# Obtener datos de las canciones
if not os.path.exists(os.path.join(carpeta_padre, 'Data', 'dataframe_songs.pkl') ):
    # Crear archivo dataFrame_albums con  la información de los albums
    __init_songs__()
