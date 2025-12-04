class restauraunt:

    def __init__(self, restauraunt_name, cuisine_type):

        self.restauraunt_name = restauraunt_name
        self.cuisine_type = cuisine_type

    def describe_restauraunt(self):

        print(f"{self.restauraunt_name} serves {self.cuisine_type} cuisine.")

    def open_restauraunt(self):

        print(f"{self.restauraunt_name} is now open!")


restaurant = restauraunt('Pizza Italia', 'pizza')
restaurant1 = restauraunt("Dominoes", "pizza")
restaurant2 = restauraunt("Little Caesers", "pizza")
restaurant3 = restauraunt("Pizza Hut", "pizza")

restaurant.describe_restauraunt()
restaurant1.describe_restauraunt()
restaurant2.describe_restauraunt()
restaurant3.describe_restauraunt()