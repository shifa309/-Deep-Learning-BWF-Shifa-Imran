Cute = {
    "name": "Cute",
    "kind": "cat",
    "owner": "Ali"
}

Tom = {
    "name": "Tom",
    "kind": "dog",
    "owner": "Alice"
}

Mithoo = {
    "name": "Mithoo",
    "kind": "Parrot",
    "owner": "Mary"
}


pets = [Cute, Tom, Mithoo]


for pet in pets:
    print("Name:", pet["name"])
    print("Kind:", pet["kind"])
    print("Owner:", pet["owner"])
    print()

