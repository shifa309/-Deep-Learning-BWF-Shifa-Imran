
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0 
    
    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine_type} restaurant.")
    
    def open_restaurant(self):
        print(f"{self.name} is now open!")
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, number):
        self.number_served += number
    
restaurant = Restaurant("Asian Wok", "Chinese")
print(f"Number of customers served originally: {restaurant.number_served}")

restaurant.number_served = 27
print(f"Number of customers served - changed: {restaurant.number_served}")

restaurant.set_number_served(200)
print(f"Number of customers served -changed again: {restaurant.number_served}")

restaurant.increment_number_served(10)
print(f"Number of customers served - incremented to previous ones: {restaurant.number_served}")
