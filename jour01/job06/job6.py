class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nom(self, nom):
        self.prenom = nom


mon_animal = Animal()


print("L'Age de l'animal", mon_animal.age,"an" )


mon_animal.vieillir()
print("L'Age de l'animal ", mon_animal.age,"an")


mon_animal.nom("Luna")
print("L'Animal se nomme ", mon_animal.prenom)
