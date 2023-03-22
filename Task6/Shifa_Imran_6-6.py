favorite_languages = {
    'Shifa': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people_to_poll = ['edward', 'sarah', 'shifa', 'ayesha', 'noor', 'Sara']

for person in people_to_poll:
    if person in favorite_languages.keys():
        print("Thank you, " + person.title()+ " for taking the poll!")
    else:
        print(person.title() + " what's your favorite programming language?")
