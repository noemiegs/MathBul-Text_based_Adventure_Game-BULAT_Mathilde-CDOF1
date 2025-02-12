import time

def introduction():
    print("Bienvenue dans l'aventure textuelle!")
    time.sleep(1)
    print("Vous êtes un jeune qui doit se rendre à l'école.")
    time.sleep(1)
    print("Vous avez deux choix: prendre le bus ou marcher.")
    time.sleep(1)

def make_choice(options):
    print("Choisissez une option:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    choice = 0
    while True:
        try:
            choice = int(input("Votre choix: "))
            if 1 <= choice <= len(options):
                break
            else:
                print(f"Veuillez choisir un numéro entre 1 et {len(options)}.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")

    
    return choice

def bus_story():
    print("\nVous décidez de prendre le bus.")
    time.sleep(1)
    print("Le bus est en retard, mais vous arrivez à l'école à temps.")
    time.sleep(1)

def walk_story():
    print("\nVous décidez de marcher jusqu'à l'école.")
    time.sleep(1)
    print("En chemin, vous trouvez une ruelle sombre.")
    time.sleep(1)
    print("Vous avez deux choix: prendre la ruelle ou rester sur le chemin principal.")

    options = ["Prendre la ruelle", "Rester sur le chemin principal"]
    choice = make_choice(options)

    if choice == 1:
        print("\nVous prenez la ruelle et découvrez un raccourci!")
        time.sleep(1)
        print("Vous arrivez à l'école plus tôt que prévu.")
    else:
        print("\nVous restez sur le chemin principal et arrivez à l'école à temps.")

def main():
    introduction()

    # Phase 1: Bus or Walk
    options_phase1 = ["Prendre le bus", "Marcher"]
    choice_phase1 = make_choice(options_phase1)

    if choice_phase1 == 1:
        bus_story()
    else:
        walk_story()

    print("\nFélicitations, vous avez terminé l'aventure textuelle!")

if __name__ == "__main__":
    main()
