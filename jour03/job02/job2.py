class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print("Détail du compte:")
        print("Numéro de compte:", self.__numero_compte)
        print("Nom:", self.__nom)
        print("Prénom:", self.__prenom)
        print("Solde:", self.__solde)
        print("Autorisation de découvert:", "Oui" if self.__decouvert else "Non")

    def afficherSolde(self):
        print("Solde du client:", self.__solde)

    def versement(self, montant):
        self.__solde += montant
        print("Versement de", montant, "effectué.")
        self.afficherSolde()

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print("Retrait de", montant, "effectué.")
        else:
            print("Solde insuffisant pour effectuer le retrait.")
        self.afficherSolde()

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = self.__solde * taux_agios
            self.__solde += agios
            print("Des agios ont été appliqués au solde du compte.")
            self.afficherSolde()

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            compte_destinataire.versement(montant)
            self.retrait(montant)
            print("Virement effectué avec succès.")
        else:
            print("Solde insuffisant pour effectuer le virement.")

# Création d'un compte bancaire
compte1 = CompteBancaire(123456789, "Lelouch", "Gilles", 1000, False)

# Appel des différentes méthodes
compte1.afficher()
compte1.versement(500)
compte1.retrait(200)
compte1.agios(0.05)

compte2 = CompteBancaire(987654321, "Potter", "Harry", -500, True)

compte1.virement(compte2, compte1.__solde)
compte1.afficher()
compte2.afficher()
