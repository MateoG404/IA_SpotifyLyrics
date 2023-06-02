import subprocess

def instalar_dependencias():
    # Lista de dependencias a instalar
    dependencias = ['numpy', 'pandas', 'matplotlib', 'spotipy']

    # Verificar si Tkinter está disponible
    try:
        import tkinter
    except ImportError:
        dependencias.append('python3-tk')

    # Instalar las dependencias
    for dependencia in dependencias:
        subprocess.check_call(['pip', 'install', dependencia])

# Llamada a la función para instalar las dependencias
instalar_dependencias()
