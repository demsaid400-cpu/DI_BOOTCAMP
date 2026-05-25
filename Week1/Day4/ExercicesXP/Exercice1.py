class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self): 
        return f"{self.name} aboie"
    def run_speed(self):
        return self.weight / self.age * 10
    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if self_power > other_power:
            return f"{self.name} a gagné le combat !"
        elif other_power > self_power:
            return f"{other_dog.name} a gagné le combat !"
        else:
            return "C'est un match nul!"
dog1 = Dog("Rex", 5, 30)
dog2 = Dog("Bella", 3, 25)
dog3 = Dog("Max", 4, 35)
print(dog1.bark())
print(dog2.bark())
print(dog3.bark())
print(f"\nVitesse de {dog1.name} : {dog1.run_speed():.2f}")
print(f"\nVitesse de {dog2.name} : {dog2.run_speed():.2f}")
print(f"\nVitesse de {dog3.name} : {dog3.run_speed():.2f}")
print(f"\n{dog1.fight(dog2)}")
print(f"{dog2.fight(dog3)}")
print(f"{dog1.fight(dog3)}")
print(dog1.bark())
