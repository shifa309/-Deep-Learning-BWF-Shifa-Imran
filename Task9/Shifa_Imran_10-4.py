file_name = 'guest_book.txt'

while True:
    name = input("What is your name? Press 'e' to exit ")
    if name == 'e':
        break
    else:
        print("Welcome, " + name.title() + "!")
        with open(file_name, 'a') as file_object:
            file_object.write(name.title() + '\n')
