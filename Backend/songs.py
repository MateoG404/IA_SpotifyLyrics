# Clase creada para extraer datos de las canciones 

from api_spotify import configuration_API_Spotify
import pandas as pd
import numpy as np
import os 
import time

class Song:
    '''
    Audio Feautures Description

    Danceability =  Danceability describes how suitable a track is for dancing based on a combination of
                    musical elements including tempo, rhythm stability, beat strength, and overall regularity.
                    A value of 0.0 is least danceable and 1.0 is most danceable.
    
    Energy =        Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and 
                    activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal 
                    has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing 
                    to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
    
    Loudness =      The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire 
                    track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound 
                    that is the primary psychological correlate of physical strength (amplitude). Values typically 
                    range between -60 and 0 db.   

    Valance =       A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high 
                    valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound 
                    more negative (e.g. sad, depressed, angry).                
    
    Get from : https://developer.spotify.com/documentation/web-api/reference/get-audio-features                    
    
    '''

    def __init__(self,id,name,danceability,energy,loudness,valance):
        self.id = id
        self.name = name
        self.danceability = danceability
        self.energy = energy
        self.loudness = loudness
        self.valance = valance
    


    #def get_audio_features():   

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
    # Conectar la API de Spotify para extraer audiofeatures
    sp = configuration_API_Spotify(ruta_config)

    for id_album in df_album['id']:
        for song in sp.album_tracks(id_album)['items']:
            audio_features = sp.audio_features(song['uri'])[0]
            print(audio_features)
        #print(sp.album(id_album).keys())

            time.sleep(10)
        #for song in ['items']:
        #    print(song)


__init__()