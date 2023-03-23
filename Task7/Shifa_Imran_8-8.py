def make_album(artist, album_title, num_tracks=None):
    album = {"artist": artist, "title": album_title}
    if num_tracks:
        album["tracks"] = num_tracks
    return album

while True:
    print("\nEnter album information (press 'q' to quit):")
    artist = input("Artist name: ")
    if artist == 'q':
        break
    album_title = input("Album title: ")
    if album_title == 'q':
        break

    album = make_album(artist, album_title)
    print(album)

