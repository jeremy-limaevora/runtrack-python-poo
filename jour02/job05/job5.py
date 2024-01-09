class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50
    
    
    def set_marque(self, marque):
        self.__marque = marque
    
    def set_modele(self, modele):
        self.__modele = modele
    
    def set_annee(self, annee):
        self.__annee = annee
    
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
    
    
    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def get_en_marche(self):
        return self.__en_marche
    
    

    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir

    

    
    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
            print("La voiture démarre.")
        else:
            print("Le réservoir est presque vide. Veuillez faire le plein.")
    
    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrête.")
    
    def __verifier_plein(self):
        return self.__reservoir > 5



ma_voiture = Voiture("Toyota", "Corolla", 2022, 5000)


ma_voiture.set_marque("Renault")
print(ma_voiture.get_marque()) 


ma_voiture.demarrer()  
ma_voiture.set_reservoir(60)
ma_voiture.demarrer() 
ma_voiture.arreter()  