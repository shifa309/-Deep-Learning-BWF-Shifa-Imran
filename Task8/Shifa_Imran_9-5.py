class User:
    def __init__(self, first_name, last_name, age, gender, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.login_attempts = 0  # added attribute

    def describe_user(self):
        print(f"\nUser profile for {self.first_name} {self.last_name}:")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Hope you are good.")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("Shifa", "Imran", 21, "Female", "Computer Scientist")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()


print(f"Login attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"Login attempts (resetted): {user.login_attempts}")

