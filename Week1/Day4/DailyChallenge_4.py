import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        # Gestion du cas où items est None
        self.items = items if items is not None else []
        self.page_size = int(page_size)
        self.total_pages = max(1, math.ceil(len(self.items) / self.page_size))
        self.current_page = 1

    def go_to_page(self, page_num):
        page_num = int(page_num)
        # Validation du numéro de page
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"La page doit être entre 1 et {self.total_pages}")
        
        self.current_page = page_num
        return self

    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = self.total_pages
        return self

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
        return self

    def previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
        return self

    def get_visible_items(self):
        # Calcul des indices basé sur le numéro de page actuel
        start = (self.current_page - 1) * self.page_size
        end = start + self.page_size
        return self.items[start:end]

# --- Zone de test corrigée ---
if __name__ == "__main__":
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabet, 4)

    try:
        print(f"Page 1: {p.get_visible_items()}")
        p.next_page().next_page()
        print(f"Après 2 'next': {p.get_visible_items()}")
        
        p.go_to_page(3)
        print(f"Aller à la page 3: {p.get_visible_items()}")
    except ValueError as e:
        print(f"Erreur : {e}")

    try:
        p.go_to_page(99)
    except ValueError as e:
        print(f"Test erreur validé : {e}")
