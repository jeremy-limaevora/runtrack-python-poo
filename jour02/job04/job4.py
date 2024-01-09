class Student:
    MAX_CREDITS = 120  

    def __init__(self, nom, prenom, numero_etudiant):
        self.nom = nom
        self.prenom = prenom
        self.numero_etudiant = numero_etudiant
        self.credits = 0
        self.level = self.calculate_level()

    def add_credits(self, credits):
        if credits > 0:
            total_credits = self.credits + credits
            if total_credits <= self.MAX_CREDITS:  
                self.credits = total_credits
                self.level = self.calculate_level()
            else:
                print("Le nombre total de crédits ne peut pas dépasser 120.")
        else:
            print("Le nombre de crédits doit être supérieur à zéro.")

    def calculate_level(self):
        if self.credits >= 90:
            return "Excellent"
        elif self.credits >= 80:
            return "Très bien"
        elif self.credits >= 70:
            return "Bien"
        elif self.credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print("Nom:", self.nom)
        print("Prénom:", self.prenom)
        print("Identifiant:", self.numero_etudiant)
        print("Niveau:", self.level)
        print("Crédits:", self.credits)



john_doe = Student("Doe", "John", 145)


john_doe.add_credits(30)
john_doe.add_credits(20)
john_doe.add_credits(20)


john_doe.student_info()
