""" Description of the functionnement of a restaurant"""

class Restaurant:
    """Make a restaurant when he's open"""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"They sell {self.cuisine_type.title()} food.")
    
    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open !")
        
    def show_number_served(self):
        print(f"The number of customers that have been served is {self.number_served}") 
    
    def set_number_served(self,served):
        """Set the number of clients served"""
        self.number_served = served 
        
    def increment_number_served(self,client):
        """Increment the number of customers served in a day"""
        self.number_served += client
    
his_restaurant = Restaurant('Shark','thai')
my_restaurant = Restaurant('Tea','british')

your_restaurant.open_restaurant()
your_restaurant.describe_restaurant()
his_restaurant.open_restaurant()
his_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()

my_restaurant.set_number_served(10)
my_restaurant.show_number_served()

my_restaurant.increment_number_served(90)
my_restaurant.show_number_served()
