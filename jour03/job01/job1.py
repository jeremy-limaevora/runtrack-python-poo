class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def set_nombre_habitants(self, nombre):
        self.__nombre_habitants = nombre


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        current_population = self.__ville.get_nombre_habitants()
        self.__ville.set_nombre_habitants(current_population + 1)



ville_paris = Ville("Paris", 1000000)
ville_marseille = Ville("Marseille", 861635)


print(f"Population de la ville de Paris : {ville_paris.get_nombre_habitants()}")
print(f"Population de la ville de Marseille : {ville_marseille.get_nombre_habitants()}")


john = Personne("John", 45, ville_paris)
myrtille = Personne("Myrtille", 4, ville_paris)
chloe = Personne("Chloé", 18, ville_marseille)


john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()


print(f"Mise a jour de la population de la ville de Paris  {ville_paris.get_nombre_habitants()}")
print(f"Mise a jour de la population de la ville de Marseille  {ville_marseille.get_nombre_habitants()}")
