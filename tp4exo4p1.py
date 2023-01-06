L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *"""
temp = 0
compte = 0
for n in range(len(L1)):
    compte=0
    for m in range(len(L1)):
        if L1[n] == L1[m]:
            compte = compte+1
        if compte > temp:
            temp = compte
            res = L1[n]
print("Le nombre le plus fréquent dans la liste est le : {} ({} x)".format(res,compte))

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *"""
