nbr=float(input("Vous cherchez la table de multiplication de quel nombre ?"))
n=0
table=0
for i in range(10):
    table=[nbr,'*',n,'=',round(nbr*n,2)]
    n = n + 1
    print(nbr,'*',n,'=',round(nbr*n,2))
