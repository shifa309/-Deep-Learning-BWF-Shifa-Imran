file_name = 'learning_python.txt'

with open(file_name) as file_object:
    contents = file_object.read()
    print(contents)

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(file_name) as file_object:
    lines = file_object.readlines()

for l in lines:
    print(l.rstrip())

