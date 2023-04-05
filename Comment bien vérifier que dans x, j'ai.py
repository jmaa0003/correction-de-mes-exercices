"""Comment bien vérifier que dans x, j'ai
des répétitions de '3*3' et me donner combien
de fois je l'ai ?"""

x = '3*3'*3**2
i = 0
count = 0
new_count = 0

if x[i:i+3] == '3*3':
    count += 1
    i = i + 1 # -- j'incrémente ma variable i pour parcourir la liste 
    # (sans oublier i + 1 pour trigger les fanas algorithmicien)--
print("Oui, il y a bien {} fois une itération de {}".format(count, x[0:3]))

if not x[i:i+3] == '3*3':
    count += 1
    print("Hélas, pas d'itération de ce genre")

    # -- jusque là, ce que j'ai fait est qu'il parcourt la séquence de x qui est
    # censée être de même longueur que '3*3' et examine si cette séquence correspond à
    # '3*3' --
    
   
    

 


"""en faire une fonction pour une iteration de a dans b quelconque"""

    