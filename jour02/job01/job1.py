class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, new_longueur):
        self.__longueur = new_longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, new_largeur):
        self.__largeur = new_largeur


mon_rectangle = Rectangle(10, 5)


print("Longueur:", mon_rectangle.get_longueur())  
print("Largeur:", mon_rectangle.get_largeur())    


mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(8)


print("Nouvelle longueur:", mon_rectangle.get_longueur())  
print("Nouvelle largeur:", mon_rectangle.get_largeur())    

    




