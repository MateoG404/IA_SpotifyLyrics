import subprocess

def instalar_dependencias():
    dependencias = ['numpy', 'pandas', 'matplotlib','spotipy']
    for dependencia in dependencias:
        subprocess.check_call(['pip', 'install', dependencia])

# Lista de dependencias a instalar


# Llamada a la función para instalar las dependencias
instalar_dependencias()
