def make_album(artist,album_name):
    album = {'artist' : artist, 'album' : album_name}
    return album 

while True:
    print("\nEnter album details or '0' to quit:")
    
    artist = input("Artist name: ")
    if artist.lower() == '0':
        break
    album_name = input("Album title: ")
    if album_name.lower() == '0':
        break
    album = make_album(artist,album_name)
    print(f"{album}")