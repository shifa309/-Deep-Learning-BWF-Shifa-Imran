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


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"\nAdmin has the following privileges:")
        for privilege in self.privileges:
            print("- " + privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age, gender, occupation):
        super().__init__(first_name, last_name, age, gender, occupation)
        self.privileges = Privileges()

        
admin = Admin("Shifa", "Imran", 30, "Feale", "Computer Scientist")
admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()

