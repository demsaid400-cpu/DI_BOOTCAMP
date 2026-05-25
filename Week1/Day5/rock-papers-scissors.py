from game import Game

def print_results(scores):
    print("\n--- RÉSULTATS FINAUX ---")
    print(f"Victoires : {scores['win']}")
    print(f"Défaites  : {scores['loss']}")
    print(f"Égalités  : {scores['draw']}")
    print("Merci d'avoir joué !")

def main():
    scores = {"win": 0, "loss": 0, "draw": 0}
    
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Jouer une nouvelle partie")
        print("2. Quitter et afficher le score")
        
        choice = input("Votre choix (1 ou 2) : ").strip()
        
        if choice == "1":
            new_game = Game()
            result = new_game.play()
            scores[result] += 1
        elif choice == "2":
            print_results(scores)
            break
        else:
            print("Option invalide, veuillez choisir 1 ou 2.")

if __name__ == "__main__":
    main()
