import math

class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur


class Cercle(Forme):
    def __init__(self, rayon):
        self.radius = rayon

    def aire(self):
        return math.pi * self.radius**2



rectangle = Rectangle(largeur=5, hauteur=3)


resultat_aire_rectangle = rectangle.aire()
print("Aire du rectangle :", resultat_aire_rectangle)


cercle = Cercle(rayon=4)


resultat_aire_cercle = cercle.aire()
print("Aire du cercle :", resultat_aire_cercle)
