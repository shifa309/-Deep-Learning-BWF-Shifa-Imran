class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


restaurant1 = Restaurant("Asian Wok", "Chinese")
restaurant2 = Restaurant("BarBQ Tonite", "Bar Bq")
restaurant3 = Restaurant("Tuscany", "Thai and Italian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
