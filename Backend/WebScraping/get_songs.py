# Este script se conecta a la API de spotify 
# y extrae las canciones de las playlist mas conocidas a nivel mundial

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import configparser
import requests 
import os

# Configurar las credenciales de acceso

# Crear una instancia de ConfigParser para acceder a las claves privadas 

config = configparser.ConfigParser()

# Obtener direccion y secciones
PATH =  os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))

config.read(PATH+'/Data/configuration/tokens.ini')

client_id = config.get("'Spotify'",'Client_ID')
client_secret = config.get("'Spotify'",'Client_secret')


# Make Auth with the Spotify API

client_credential_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credential_manager)

# 
playlist_id = '37i9dQZF1DX2piJKuRdKIA'

playlist = sp.playlist(playlist_id)
print(type(playlist),playlist.keys())

print()

print(playlist['description'])

