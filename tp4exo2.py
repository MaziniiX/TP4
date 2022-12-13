# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []
somme=0
for i in range(nombreEtudiants):
    noteI=float(input("Note etudiant {} : ".format(i)))
    if noteI<0 or noteI>20:
        while noteI<0 or noteI>20:
            print("Saisissez une note différente de 0 et de 20")
            noteI=float(input("Note etudiant {} : ".format(i)))
    notes.append(noteI)
    somme+=noteI
print()
moyenne=somme/nombreEtudiants
print("Moyenne de classe :",moyenne)
print()
print("Numéro de l'Etudiant | note | ecart a la moyenne")
for n in range(nombreEtudiants):
    print("{} | {} | {}".format(n,notes[n],notes[n]-moyenne))