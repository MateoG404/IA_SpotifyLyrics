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



def __init__():
        
    # Abrir archivo dataframe con información de los albumes
    PATH_URL = os.path.join(get_PATH_URL(), 'Data', 'dataframe_albums.pkl')
    df_album =  pd.read_pickle(PATH_URL)

    
    array_songs =  []
    ruta_config = os.path.join(get_PATH_URL(), 'Backend/Tokens', 'tokens.ini')

    if not os.path.exists(ruta_config):
        raise FileNotFoundError(f"El archivo config.ini no se encuentra en la ruta: {ruta_config}")
    
    print(ruta_config)
    clientID = 'c44fa7630d8f42cda23b8ab3f5479fa5' #'c4a67065bd544df2b4127e3cbc17b6f6' #config['spotify']['client_id']

    clientSecret ='3a47c89550f5465f8f4bdcec4ae1a8c1' # 'b81c2f7d01d24488b431bbb05976e77a' #config['spotify']['client_secret']

    # Make Auth with the Spotify API

    client_credential_manager = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
    sp = spotipy.Spotify(client_credentials_manager = client_credential_manager)

    # Conectar la API de Spotify para extraer audiofeatures
    sp = configuration_API_Spotify(ruta_config)

    
    # Crear DataFrame para las canciones

    songs_id = [] 
                        # id,duration_ms, danceability, energy, loudness, valence,
    audio_features_df = []
    cont = 1
    cont_album = 0
    
    
    for id_album in df_album['id']:
        print(cont_album)
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
    
__init__()