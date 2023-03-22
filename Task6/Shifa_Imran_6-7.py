# Define a dictionary representing a person
person1 = {
    "first_name": "Shifa",
    "last_name": "Imran",
    "age": 21,
    "city": "Islamabad"
}

# Define a dictionary representing another person
person2 = {
    "first_name": "Maryam",
    "last_name": "Ahmad",
    "age": 19,
    "city": "Faisalabad"
}

person3 = {
    "first_name": "Ali",
    "last_name": "Ishan",
    "age": 40,
    "city": "Lahore"
}

people = [person1, person2, person3]

for person in people:
    print("First Name:", person["first_name"])
    print("Last Name:", person["last_name"])
    print("Age:", person["age"])
    print("City:", person["city"])
    print()
