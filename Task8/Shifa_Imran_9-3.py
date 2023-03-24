class User:
    def __init__(self, first_name, last_name, age, gender, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation

    def describe_user(self):
        print(f"\nUser profile for {self.first_name} {self.last_name}:")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Hope you are good.")

user1 = User("Shifa", "Imran", 21, "Female", "Computer Scientist")
user2 = User("Noor", "Ahmad", 25, "Female", "Graphic Designer")
user3 = User("Maryam", "Ali", 45, "Feale", "Media manager")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

