class Ville:
    def __init__(self, nom, population):
        self.__nom = nom
        self.__population = population

    def get_population(self):
        return self.__population


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        self.__ville.__population += 1


paris = Ville("Paris", 1000000)


print("Nombre d'habitants de la ville de Paris:", paris.get_population())


marseille = Ville("Marseille", 861635)


print("Nombre d'habitants de la ville de Marseille:", marseille.get_population())


john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)