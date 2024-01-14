class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("Âge de la personne:", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("J'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=14):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")



personne = Personne()
personne.afficherAge()
personne.bonjour()


eleve = Eleve()
eleve.afficherAge()
eleve.allerEnCours()


professeur = Professeur(matiereEnseignee="Histoire/Géographie")
professeur.afficherAge()
professeur.enseigner()
