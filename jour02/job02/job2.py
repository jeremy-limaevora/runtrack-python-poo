class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    def get_titre(self):
        return self.__titre

    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def set_nb_pages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Le nombre de pages doit être un entier positif.")


mon_livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 100)


print("Titre:", mon_livre.get_titre())       
print("Auteur:", mon_livre.get_auteur())     
print("Nombre de pages:", mon_livre.get_nb_pages())  


mon_livre.set_nb_pages(-50)  


mon_livre.set_nb_pages(120)


print("Nouveau nombre de pages:", mon_livre.get_nb_pages())  
