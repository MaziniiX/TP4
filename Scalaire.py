nMax=10
v1=[]
v2=[]
resultat=0
n=int(input("Quelle est la taille de vos vecteurs [entre 1 et {}] ?".format(nMax)))
while 1>n>nMax:
    int(input("Quelle est la taille de vos vecteurs [entre 1 et {}] ?".format(nMax)))
print("Saisie du premier vecteur :")
for i in range(n):
    v1.append(float(input("v1[{}] = ".format(i))))
print()
print("Saisie du second vecteur :")
for i in range(n):
    v2.append(float(input("v2[{}] = ".format(i))))
for i in range(n):
    produit=(v1[i]*v2[i])
    resultat=resultat+produit
print()
print("Le produit scalaire de v1 par v2 vaut {}".format(resultat))