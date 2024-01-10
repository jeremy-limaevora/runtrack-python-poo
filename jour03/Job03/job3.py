class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"Titre: {self.titre}\nDescription: {self.description}\nStatut: {self.statut}\n"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.statut = "Terminée"

    def afficherListe(self):
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        filtered_list = [tache for tache in self.taches if tache.statut == statut]
        return filtered_list



tache1 = Tache("T1", "Faire les courses", "À faire")
tache2 = Tache("T2", "Jouez", "À faire")
tache3 = Tache("T3", "Dormir", "Terminé")


liste_taches = ListeDeTaches()


liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)


print("Liste de toutes les tâches :")
liste_taches.afficherListe()


liste_taches.marquerCommeFinie(tache2)


print("\nListe des tâches à faire :")
taches_a_faire = liste_taches.filterListe("À faire")
for tache in taches_a_faire:
    print(tache)


liste_taches.supprimerTache(tache1)


print("\nListe de toutes les tâches après suppression :")
liste_taches.afficherListe()