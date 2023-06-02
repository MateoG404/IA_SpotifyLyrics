# Archivo creado para conectar y obtener los audiofeatures de las canciones de spotify

#Librerias Spotify
import spotipy
import configparser
from spotipy.oauth2 import SpotifyClientCredentials

# Librerias para manejo de datos
import pandas as pd
import numpy as np
import os   

# Obtener ruta de archivo 
def get_PATH_URL():
    ruta_config = os.path.join( os.getcwd(), 'Tokens', 'tokens.ini')
    carpeta_padre = os.path.dirname( os.getcwd())
    return ruta_config,carpeta_padre
 
# Configuración para usar la API de Spotify
def configuration_API_Spotify(ruta_config):
    # Configuration API Spotify

    config = configparser.ConfigParser()
    config.read(ruta_config)

    # Obtener Tokens
    clientID = config.get('Spotify', 'ClientID')
    clientSecret = config.get('Spotify', 'Client_secret')
    print(clientID)

    # Make Auth with the Spotify API
    client_credential_manager = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
    sp = spotipy.Spotify(client_credentials_manager = client_credential_manager)
    return sp

# Obtener información de los albums haciendo uso de la API
def get_info_albums(PATH_URL,sp):

    file_url = open(PATH_URL,'r')
    lines_url = file_url.readlines()
    array_album_info = []

    for line in lines_url :        
        linea_nueva = line.replace("https://open.spotify.com/album/","")
        linea_nueva = linea_nueva[:linea_nueva.find("?si")]
        
        # Get the album information from Spotify
        album = sp.album(linea_nueva)
        array_album_info.append([album['id'],album['total_tracks'],album['name'],album['artists'][0]['name'],album['tracks']])

    return pd.DataFrame(columns = ['id','total_tracks','name_album','name_artist','tracks'],data = array_album_info)

# Función para ejecutar la extración de datos de los albums
def __init__():
        
    # Obtener la ruta completa del archivo con las URL
    ruta_config,carpeta_padre = get_PATH_URL()
    PATH_URL = os.path.join(carpeta_padre, 'Data', 'URLS_Spotify.txt')

    # Verificar si el archivo config.ini existe
    if not os.path.exists(ruta_config):
        raise FileNotFoundError(f"El archivo config.ini no se encuentra en la ruta: {ruta_config}")

    # Configurar la API de Spotify para obtener los datos
    sp = configuration_API_Spotify(ruta_config)

    # Obtener la información de los albums de Spotify
    df_albums = get_info_albums(PATH_URL,sp)

    # Guardar df en un archivo binario
    df_albums.to_pickle(os.path.join(carpeta_padre, 'Data', 'dataframe_albums.pkl'))
