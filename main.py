"""
    Nom: Gabriel Foriel Fusier
    Groupe: 401
    Description: Jeu de devinettes (il faut trouver un nombre d'un minimum a un maximum, choisient par le joueur)
"""
import random
def game(min, max):
    print(f"J’ai choisi un nombre au hasard entre {min} et {max}. À vous de le deviner...")
    hidden_value = random.randint(min, max)
    num_attempt = 0
    playing = True
    while playing:
        attempt = int(input("Entrez votre essai: "))
        num_attempt += 1
        if attempt > hidden_value:
            print(f"Mauvais choix, le nombre est plus petit que {attempt}")
        elif attempt < hidden_value:
            print(f"Mauvaise réponse, le nombre est plus grand que {attempt}")
        else:
            print(f"Bravo! Bonne réponse\nVous avez réussi en {num_attempt}  essai(s). ")
            playing = False

retry = True
while retry:
    min = int(input("Quel est le minimum: "))
    max = int(input("Quel est le maximum: "))
    game(min, max)
    retry = str(input("Voulez-vous faire une autre partie (o/n)? "))
    if retry == "n":
        print("Merci et au revoir…")
        retry = False
