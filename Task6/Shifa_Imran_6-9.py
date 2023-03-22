favorite_places = {
    "Ali": ["Paris", "New York", "UK"],
    "Mary": ["Singapore", "Germany"],
    "Abdullah": ["Pakistan", "India"]
}

for name, places in favorite_places.items():
    print(name + "'s favorite places are:")
    for place in places:
        print(": " + place)
    print()
