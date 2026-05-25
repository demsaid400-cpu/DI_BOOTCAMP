class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name
def is_18(self):
        return self.age >= 18
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []
        
    def born(self, first_name, age):
            self.members.append({"name": first_name, "age": age})
         
    def family_presentation(self):
        print(f"\nFamily {self.last_name} :")
        for m in self.members:
          print(f"{m['name']} - {m['age']} ans")
             
    def check_majority(self, first_name):
     for m in self.members:
        if m["name"] == first_name:
         if m["age"] >= 18:
            print(f"{first_name} est majeur.")
         else:
            print(f"{first_name} est mineur.")
         return
     print(f"{first_name} n'existe pas dans la famille.")
        
family = Family("Dupont")
family.born("Alice", 25)
family.born("Bob", 15)
family.born("Charlie", 18)
family.born("Diana", 10)
        
print("\n--- Vérification de majoritéS ---")
family.check_majority("Alice")
family.check_majority("Bob")
family.check_majority("Charlie")
family.check_majority("Diana")
