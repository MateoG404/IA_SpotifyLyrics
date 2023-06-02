
# Librerias

from dependences import instalar_dependencias
from api_spotify import __init__
from songs import __init_songs__
from Kmeans_clasificador import __init_clasificador__
from RandomForest import __init_random_forest
import os
import pandas as pd
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
    __init__()

# Obtener datos de las canciones
if not os.path.exists(os.path.join(carpeta_padre, 'Data', 'dataframe_songs.pkl') ):
    __init_songs__()
else:
    df = pd.read_pickle(os.path.join(carpeta_padre, 'Data', 'dataframe_songs.pkl'))

# Hacer clasificación manual de las canciones
if not os.path.exists(os.path.join(carpeta_padre, 'Data', 'dataframe_songs_sentimientos.pkl') ):
    __init_clasificador__()

# Entrenar modelo Random Forest
if not os.path.exists(os.path.join(carpeta_padre, 'Data', 'random_forest_model.joblib') ):
    __init_random_forest()


print(df)