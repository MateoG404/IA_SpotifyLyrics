# Code que realiza la clasificación de sentimientos
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from Kmeans_clasificador import get_dfSongs
from songs import get_PATH_URL
import os
import pickle as pickle


def random_forest(df):
    
    # Seleccionar las características de audio como variables predictoras
    X = df[['energy', 'valence']]

    # Seleccionar la columna 'sentimiento' como variable objetivo
    y = df['sentimiento']

    # Dividir el conjunto de datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear el modelo de Random Forest
    random_forest = RandomForestClassifier(random_state=42)

    scores = cross_val_score(random_forest, X, y, cv=5)

    # Imprimir los resultados de la validación cruzada

    print("Resultados de la validación cruzada:")
    for i, score in enumerate(scores):
        print("Fold {}: {:.2f}%".format(i+1, score * 100))

    # Calcular el promedio de los resultados
    mean_score = scores.mean()
    print("Precisión promedio: {:.2f}%".format(mean_score * 100))

    # Entrenar el modelo
    random_forest.fit(X,y)

    return random_forest

def predict_feeling_song(data):
    # Cargar modelo

    saved_model = pickle.load( open(os.path.join(get_PATH_URL(), 'Data', 'random_forest_model2.joblib'), "rb"))

    print(saved_model.predict(data))

    

def __init_random_forest():
        
    # Cargar el DataFrame con las características de audio y etiquetas de sentimientos
    df = get_dfSongs('dataframe_songs_sentimientos.pkl')

    '''
        IMPLEMENTACIÓN ALGORITMO RANDOM FOREST
    '''
    random_forest_spotify = random_forest(df)

    # Guardar modelo
    pickle.dump(random_forest_spotify, open(os.path.join(get_PATH_URL(), 'Data', 'random_forest_model2.joblib'), "wb"))

    ''' 
        GUARDADO DE MODELO
    '''

    joblib.dump(random_forest, os.path.join(get_PATH_URL(), 'Data', 'random_forest_model.joblib'))

#__init_random_forest()



