def VerificationDate(date):
  if len(date) != 8:
    print("Format de date incorrect. Veuillez entrer la date au format jjmmaaaa.")
    return

  jour = int(date[:2])
  mois = int(date[2:4])
  annee = int(date[4:])

  bissextile = False
  if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    bissextile = True
  if mois in [1, 3, 5, 7, 8, 10, 12]:
    if jour < 1 or jour > 31:
      print("Date incorrecte.")
      return
  elif mois in [4, 6, 9, 11]:
    if jour < 1 or jour > 30:
      print("Date incorrecte.")
      return
  elif mois == 2:
    if bissextile:
      if jour < 1 or jour > 29:
        print("Date incorrecte.")
        return
    else:
      if jour < 1 or jour > 28:
        print("Date incorrecte.")
        return
  else:
    print("Date incorrecte.")
    return
  print("Date correcte.")

VerificationDate("29022012")
VerificationDate("30022012")
VerificationDate("28022011")
VerificationDate("28022013")
