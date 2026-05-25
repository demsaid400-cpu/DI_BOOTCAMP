import random

class Game:
    def __init__(self):
        self.choices = ["pierre", "papier", "ciseaux"]

    def get_user_item(self):
        while True:
            user_input = input("Choisissez pierre, papier, ou ciseaux : ").lower().strip()
            if user_input in self.choices:
                return user_input
            print("Choix invalide. Veuillez recommencer.")

    def get_computer_item(self):
        return random.choice(self.choices)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        
        win_conditions = {
            "pierre": "ciseaux",
            "papier": "pierre",
            "ciseaux": "papier"
        }
        
        return "win" if win_conditions[user_item] == computer_item else "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"\nVous : {user_item} | Ordinateur : {computer_item}")

        if result == "win":
            print("Résultat : Vous avez gagné !")
        elif result == "loss":
            print("Résultat : L'ordinateur a gagné !")
        else:
            print("Résultat : Égalité !")
        
        return result
