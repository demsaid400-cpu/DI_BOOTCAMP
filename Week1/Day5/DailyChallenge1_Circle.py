import math
import pandas as pd


class Circle:

    # Initialisation avec le rayon
    def __init__(self, radius):
        self.radius = radius

    # =========================
    # DECORATORS
    # =========================

    # Obtenir le diamètre
    @property
    def diameter(self):
        return self.radius * 2

    # Modifier le diamètre
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    # =========================
    # METHODES
    # =========================

    # Calcul de l’aire
    def area(self):
        return math.pi * (self.radius ** 2)

    # Affichage du cercle
    def __str__(self):
        return (
            f"Circle(radius={self.radius}, "
            f"diameter={self.diameter}, "
            f"area={self.area():.2f})"
        )

    # =========================
    # DUNDER METHODS
    # =========================

    # Addition de deux cercles
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    # Comparaison >
    def __gt__(self, other):
        return self.radius > other.radius

    # Comparaison ==
    def __eq__(self, other):
        return self.radius == other.radius

    # Comparaison < (pour le tri)
    def __lt__(self, other):
        return self.radius < other.radius


# =========================
# CREATION DES CERCLES
# =========================

circle1 = Circle(5)
circle2 = Circle(3)
circle3 = Circle(8)

# =========================
# AFFICHAGE
# =========================

print("=== AFFICHAGE DES CERCLES ===")
print(circle1)
print(circle2)
print(circle3)

# =========================
# RAYON ET DIAMETRE
# =========================

print("\n=== RAYON ET DIAMETRE ===")
print("Rayon circle1 :", circle1.radius)
print("Diamètre circle1 :", circle1.diameter)

# Modifier le diamètre
circle1.diameter = 20

print("Nouveau diamètre :", circle1.diameter)
print("Nouveau rayon :", circle1.radius)

# =========================
# AIRE
# =========================

print("\n=== AIRE ===")
print("Aire de circle1 :", circle1.area())

# =========================
# ADDITION
# =========================

print("\n=== ADDITION ===")

new_circle = circle1 + circle2

print("Nouveau cercle :", new_circle)

# =========================
# COMPARAISONS
# =========================

print("\n=== COMPARAISONS ===")

print("circle1 > circle2 :", circle1 > circle2)
print("circle1 == circle2 :", circle1 == circle2)

# =========================
# TRI DES CERCLES
# =========================

print("\n=== TRI DES CERCLES ===")

circles = [circle1, circle2, circle3, new_circle]

circles.sort()

for circle in circles:
    print(circle)

# =========================
# PANDAS DATAFRAME
# =========================

print("\n=== DATAFRAME PANDAS ===")

data = {
    "Radius": [c.radius for c in circles],
    "Diameter": [c.diameter for c in circles],
    "Area": [round(c.area(), 2) for c in circles]
}

df = pd.DataFrame(data)

print(df)
