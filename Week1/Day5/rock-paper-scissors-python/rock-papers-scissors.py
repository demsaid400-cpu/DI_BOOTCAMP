from game import Game

def print_results(scores):
    print("\n" + "="*20)
    print("  SCORE FINAL")
    print("="*20)
    print(f"Victoires : {scores['win']}")
    print(f"Défaites  : {scores['loss']}")
    print(f"Égalités  : {scores['draw']}")
    print("="*20)
    print("Merci d'avoir joué !")

def main():
    scores = {"win": 0, "loss": 0, "draw": 0}
    
    while True:
        print("\n--- PIERRE-PAPIER-CISEAUX ---")
        print("1. Jouer une partie")
        print("2. Quitter et voir le score")
        
        choice = input("\nVotre choix (1/2) : ").strip()
        
        if choice == "1":
            new_game = Game()
            result = new_game.play()
            scores[result] += 1
        elif choice == "2":
            print_results(scores)
            break
        else:
            print("Erreur : Entrez 1 ou 2.")

if __name__ == "__main__":
    main()
