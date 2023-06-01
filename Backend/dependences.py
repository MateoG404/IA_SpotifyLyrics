import subprocess

def instalar_dependencias():
    # Lista de dependencias a instalar
    dependencias = ['numpy', 'pandas', 'matplotlib','spotipy']
    for dependencia in dependencias:
        subprocess.check_call(['pip', 'install', dependencia])



# Llamada a la función para instalar las dependencias
instalar_dependencias()
