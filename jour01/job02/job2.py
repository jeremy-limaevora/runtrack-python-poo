class opération :
    
    def __init__(self,nombre1= 12,nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        return self.nombre1 + self.nombre2

opération = opération()

print ("le nombre1 est " + 
       str(opération.nombre1))
print ("le nombre2 est " + 
       str(opération.nombre2))



