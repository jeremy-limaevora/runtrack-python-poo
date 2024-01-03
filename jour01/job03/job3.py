class opération :
    
    def __init__(self,nombre1= 12,nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        return self.nombre1 + self.nombre2

opération_instance = opération()
resultat_addition = opération_instance.addition()

print("Le resultat de l'addition est :",resultat_addition)