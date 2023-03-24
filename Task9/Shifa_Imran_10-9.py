filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename, 'r') as file:
            print(f"\nContents of {filename}:")
            contents = file.read()
            print(contents)
    except FileNotFoundError:
		#fail silently if either file is missing
        pass

