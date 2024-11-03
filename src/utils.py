import time

def log_error(message):
    """Enregistre un message d'erreur dans le fichier logs.txt"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("data/logs.txt", "a") as file:
        file.write(f"[{timestamp}] {message}\n")