#Créer notre répertoire 
repertoire = ['A','C','D']

print(f"Hello {repertoire[0]}, I invite you,{repertoire[1]} and {repertoire[2]} to diner")

print(f"Hello {repertoire[1]}, I invite you, {repertoire[0]} and {repertoire[2]} to diner")

print(f"Hello {repertoire[2]}, I invite you, {repertoire[1]} and {repertoire[0]} to diner. So we will be {len(repertoire)} !")

#Enlève le contact C de la liste des invités
not_present = 'C';
repertoire.remove(not_present);
print(f"{not_present} cannot come this day");
print(len(repertoire));

#Ajoute le contact E à la liste des invités
repertoire.append('E');
print(f"Consequently, I add {repertoire[2]} in place of him")

# Ajoute au premier, quatrième emplacement du répertoire 
print(f"I found a bigger dinner table so the list of invits are :")
new_invit_1 = repertoire.insert(0, 'H')
new_invit_2 = repertoire.insert(3,'I')
new_invit_3 = repertoire.append('J')

print(f"{repertoire[0]},{repertoire[1]},{repertoire[2]},{repertoire[3]},{repertoire[4]},{repertoire[5]}");

print("Finally, my new dinner table can't arrive in time for the dinner.");
print(f"So, we will be {len(repertoire)}");

#Supprime H,I,E,J du répertoire des invités
cannot_invit_1 = repertoire.pop(0)
cannot_invit_2 = repertoire.pop(4)
cannot_invit_3 = repertoire.pop(2)
cannot_invit_4 = repertoire.pop(2)

print(f"I'm really apologize for the troubles, {cannot_invit_1}, {cannot_invit_2}, {cannot_invit_3}, {cannot_invit_4}")

print(f"So {repertoire[0]} and {repertoire[1]} can come")
print(f"So, we will be {len(repertoire)}")

#Supprime A et D pour une autre fois ! 
del repertoire[0] 
del repertoire[0]


