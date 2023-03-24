file_name = 'responses.txt'

print("Why do you like programming? Press 'e' to exit")

while True:
    answer = input(": ")
    if answer == 'e':
        break
    else:
        with open(file_name, 'a') as file_object:
            file_object.write(answer + '\n')
            print("Response written to file.")
