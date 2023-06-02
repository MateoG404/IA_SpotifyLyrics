'''

    Este código esta creado para etiquetar un sentimiento a las canciones de acuerdo a las variables danceability, energy, loudness, valence usando K-means

'''

from songs import get_PATH_URL
import os
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline


def get_dfSongs():
    PATH_URL = os.path.join(get_PATH_URL(), 'Data', 'dataframe_songs.pkl')
    df_songs = pd.read_pickle(PATH_URL)
    return df_songs

def kmeans_clasification(df):

    # Obtener los features de las canciones 
    
    features = df[['valence', 'energy']]
    
    # Aplicar el algoritmo de clustering K-means para clasificar las canciones en categorías
    kmeans = KMeans(n_clusters=2, random_state=42)
    kmeans.fit(features)

    # Obtener las etiquetas de sentimientos asignadas por el algoritmo de clustering
    labels = kmeans.labels_

    # Crear un diccionario para mapear las etiquetas a categorías de sentimientos donde 0 representa Tristeza y 1 Alegria
    sentiment_map = {0: 'Tristeza', 1: 'Alegría'}

    # Agregar las categorías de sentimientos al DataFrame original
    df['sentimiento'] = [sentiment_map[label] for label in labels]

    # Crear un gráfico de dispersión para visualizar los resultados del clustering
    
    plt.scatter(df['valence'], df['energy'], c=labels, cmap='seismic')
    plt.legend(handles=[plt.scatter([], [], c='blue', label='Tristeza'),
                    plt.scatter([], [], c='red', label='Alegría')],loc='upper right')
    plt.xlabel('Valence')
    plt.ylabel('Energy')
    plt.title('Clustering de Sentimientos')
    plt.show()
    return df

def __init_clasificador__():
    
    df_songs = get_dfSongs()

    df_feelings_songs = kmeans_clasification(df_songs)
    df_feelings_songs.to_pickle(os.path.join(get_PATH_URL(), 'Data', 'dataframe_songs_sentimientos.pkl'))

__init_clasificador__()