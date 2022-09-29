def make_album(artist_name, album_title,nb = None):
    music_album = {'name':artist_name,'title':album_title}
    
    if nb: #si le nombre de clips dans l'album est défini, créer une valeur-clé dans le dictionnaire
        music_album['nombre'] = nb
    return music_album

album_1 = make_album('stromae','formidable',nb=3)
print(album_1)
album_2 = make_album('black m','brisé',nb=3)
print(album_2)
album_3 = make_album('freeze corleone','ekip',nb=4)
print(album_3)

