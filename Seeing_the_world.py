#Liste de villes dans le monde à visiter

locations = ['Paris','Londres','Madrid','Rome','Berlin'];
print(locations);

# Affichage du classement alphabétique des villes #

print(sorted(locations));

#Vérification de la non modification des listes#
print(locations);

# changement temporaire de l'ordre de la liste par inversion 
locations.reverse();
print(locations);

# retour temporaire de l'ordre original de la liste
locations.reverse();
print(locations);

#changement définitif de l'ordre de la liste

locations.sort();
print(locations);

#changement définitif de l'ordre alphabétique de la liste par inversion
locations.sort(reverse=True);
print(locations);