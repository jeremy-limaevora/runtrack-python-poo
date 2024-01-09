class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True  

    
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

  
    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté ou est déjà disponible.")


mon_livre = Livre("Les Misérables", "Victor Hugo", 1000)

print("Titre:", mon_livre.get_titre())       
print("Auteur:", mon_livre.get_auteur())     
print("Nombre de pages:", mon_livre.get_nb_pages())  


mon_livre.emprunter()


mon_livre.rendre()
