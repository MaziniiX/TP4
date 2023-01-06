def VerificationDate(date):
  # Vérifier si la date est au bon format (jjmmaaaa)
  if len(date) != 8:
    print("Format de date incorrect. Veuillez entrer la date au format jjmmaaaa.")
    return

  # Extraire le jour, le mois et l'année de la date
  jour = int(date[:2])
  mois = int(date[2:4])
  annee = int(date[4:])

  # Vérifier si l'année est bissextile
  bissextile = False
  if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    bissextile = True

  # Vérifier si le jour est valide en fonction du mois et de l'année
  if mois in [1, 3, 5, 7, 8, 10, 12]:
    # Les mois de janvier, mars, mai, juillet, août, octobre et décembre ont 31 jours
    if jour < 1 or jour > 31:
      print("Date incorrecte.")
      return
  elif mois in [4, 6, 9, 11]:
    # Les mois de avril, juin, septembre et novembre ont 30 jours
    if jour < 1 or jour > 30:
      print("Date incorrecte.")
      return
  elif mois == 2:
    # Le mois de février a 28 jours dans les années communes et 29 jours dans les années bissextiles
    if bissextile:
      if jour < 1 or jour > 29:
        print("Date incorrecte.")
        return
    else:
      if jour < 1 or jour > 28:
        print("Date incorrecte.")
        return
  else:
    # Si le mois n'est pas valide, la date est incorrecte
    print("Date incorrecte.")
    return

  # Si aucun cas de date incorrecte n'a été détecté, la date est correcte
  print("Date correcte.")

# Tester le programme avec plusieurs dates
VerificationDate("29022012") # Date correcte
VerificationDate("30022012") # Date incorrecte
VerificationDate("28022011") # Date correcte
VerificationDate("28022013") # Date incorrecte
