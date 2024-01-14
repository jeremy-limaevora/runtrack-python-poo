class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    def get_longueur(self):
        return self._longueur

    def set_longueur(self, nouvelle_longueur):
        self._longueur = nouvelle_longueur

    def get_largeur(self):
        return self._largeur

    def set_largeur(self, nouvelle_largeur):
        self._largeur = nouvelle_largeur

    def perimetre(self):
        return 2 * (self._longueur + self._largeur)

    def surface(self):
        return self._longueur * self._largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur

    def get_hauteur(self):
        return self._hauteur

    def set_hauteur(self, nouvelle_hauteur):
        self._hauteur = nouvelle_hauteur

    def volume(self):
        return self._longueur * self._largeur * self._hauteur



rectangle = Rectangle(longueur=5, largeur=3)
print("Perimètre du rectangle:", rectangle.perimetre())
print("Surface du rectangle:", rectangle.surface())


rectangle.set_longueur(8)
rectangle.set_largeur(4)
print("Nouvelle longueur du rectangle:", rectangle.get_longueur())
print("Nouvelle largeur du rectangle:", rectangle.get_largeur())


parallelepipede = Parallelepipede(longueur=5, largeur=3, hauteur=2)
print("Volume du parallélépipède:", parallelepipede.volume())
