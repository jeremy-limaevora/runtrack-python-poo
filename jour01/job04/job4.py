class Personne :
    
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom

    def Sepresenter(self):
        print("Je suis",self.nom, self.prenom)

personne = Personne("John","Doe")
personne.Sepresenter()
personne = Personne("Jean","Dupont")
personne.Sepresenter()



  

