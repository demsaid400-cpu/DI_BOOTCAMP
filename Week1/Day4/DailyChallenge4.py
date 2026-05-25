import math
class Pagination:
    def  __init__(self, items, page_size):
        self.items =items
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / page_size)

    def get_visible_items(self):
       start = self.current_idx
       end = start + self.page_size
       return self.items[start:end]
def go_to_page(self, page_num):
     if page_num < 1 or page_num > self.total_pages:
      raise  ValueError(f"Page {page_num} est hors limites. Total pages:{self.total_pages}")
      self.current_idx = (page_num - 1) * self.page_size
      return self

    def first_page(self):
     self.current_idx = 0
     return self

    def last_page(self):
     self.current_idx = (self.total_pages - 1) * self.page_size
     return self
      def next_page(self):
     if self.current_idx + self.page_size < len(self.items):
        self.current_idx += self.page_size
     return self

    def previous_page(self):
     if self.current_idx - self.page_size >= 0:
        self.current_idx -= self.page_size
        return self
    
    def __str__(self):
     return "\n".join(str(item) for item in self.get_visible_items())

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print("Page 1:")
print(p.get_visible_items())
p.next_page()
print("\nPage 2:")
print(p.get_visible_items())

p.last_page()
print("n\Dernière page:")
print(p.get_visible_items())

print("\n--- String representtion ---")
p.first_page()
print(str(p))

print("\n--- Test erreur ---")
try:
    p.go_to_page(10)
except ValueError as e:
    print(f"Erreur: {e}")
      
try: 
    p.go_to_page(0)
except ValueError as e:
print(f"Erreur: {e}")
