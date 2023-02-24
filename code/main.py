# Auteur : Paul-Loup Germain
# Date : 23.02.2023
# Project : chat alert main.py

import datetime
import time

while True:
    # Vérifiez si nous sommes en semaine et qu'il est 18h00
    now = datetime.datetime.now()
    if now.weekday() < 5 and now.hour == 18:
        # Allumez l'ours en peluche
        
    else:
        # Éteignez l'ours en peluche
        

    # Attendez 1 minute avant de vérifier à nouveau l'heure
    time.sleep(60)

