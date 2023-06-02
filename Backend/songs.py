# Clase creada para extraer datos de las canciones 

from api_spotify import configuration_API_Spotify
import pandas as pd
import numpy as np
import os 
import time
import spotipy
import configparser
from spotipy.oauth2 import SpotifyClientCredentials



def get_PATH_URL():
    carpeta_padre = os.path.dirname(os.getcwd())
    return carpeta_padre



def __init_songs__():
        
    # Abrir archivo dataframe con información de los albumes
    PATH_URL = os.path.join(get_PATH_URL(), 'Data', 'dataframe_albums.pkl')
    df_album =  pd.read_pickle(PATH_URL)

    
    array_songs =  []
    ruta_config = os.path.join(get_PATH_URL(), 'Backend/Tokens', 'tokens.ini')

    if not os.path.exists(ruta_config):
        raise FileNotFoundError(f"El archivo config.ini no se encuentra en la ruta: {ruta_config}")
    
    # Conectar la API de Spotify para extraer audiofeatures
    sp = configuration_API_Spotify(ruta_config)

    
    # Crear DataFrame para las canciones

    songs_id = [] 
                        # id,duration_ms, danceability, energy, loudness, valence,
    audio_features_df = []
    cont = 1
    cont_album = 0
    
    
    for id_album in df_album['id']:
        for song in sp.album_tracks(id_album)['items']:
            try:
                audio_features = sp.audio_features(song['uri'])[0]
                songs_id.append(audio_features['id'])
                audio_features_df.append([song['name'],audio_features['duration_ms'],audio_features['danceability'],audio_features['energy'],audio_features['loudness'],audio_features['valence']])
            
            except:
                # Guardar temp
                df_songs = pd.DataFrame(columns = ['id','duration_ms','danceability','energy','loudness','valence'],data = audio_features_df,index = songs_id)
                df_songs.to_pickle(os.path.join(get_PATH_URL(), 'Data', 'dataframe_songs.pkl'))

                time.sleep(30)
                pass

        cont_album += 1

    df_songs = pd.DataFrame(columns = ['id','duration_ms','danceability','energy','loudness','valence'],data = audio_features_df,index = songs_id)
    print(df_songs) 
    df_songs.to_pickle(os.path.join(get_PATH_URL(), 'Data', 'dataframe_songs.pkl'))
