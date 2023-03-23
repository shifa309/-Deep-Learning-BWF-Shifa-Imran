def make_album(artist, album_title, num_tracks=None):
    album = {"artist": artist, "title": album_title}
    if num_tracks:
        album["tracks"] = num_tracks
    return album

album1 = make_album("Queen", "A Night at the Opera")
album2 = make_album("The Beatles", "Abbey Road")
album3 = make_album("Led Zeppelin", "Led Zeppelin IV", 8)

print(album1)
print(album2)
print(album3)
