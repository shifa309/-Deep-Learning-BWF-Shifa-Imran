#modifiying example program on pg 113 114 a bit

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'age': 34
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'age': 28
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    age = user_info['age']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    print(f"\tAge: {age}")

