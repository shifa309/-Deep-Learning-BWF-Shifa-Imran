def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingr in ingredients:
        print("-", ingr)
    print("Sandwich is ready!\n")

make_sandwich("egg")
make_sandwich("chicken spread", "cheese", "cabbage")
make_sandwich("spread", "chicken", "bread", "lettuce", "tomato")

