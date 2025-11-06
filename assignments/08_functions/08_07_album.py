def make_album(artist,album_name,songs=None):
    album = {'artist' : artist, 'album' : album_name}
    if songs:
        album['songs'] = songs
    return album

playlist_1 = make_album('The Beatles','Abbey Road')
print(playlist_1)

playlist_2 = make_album('Nirvania','Nevermind')
print(playlist_2)

playlist_3 = make_album('Frank Sinatra','Ultimate Sinatra',songs = '26')
print(playlist_3)