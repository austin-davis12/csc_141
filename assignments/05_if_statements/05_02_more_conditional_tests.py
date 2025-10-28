car = 'audi'
car == 'audi'
True
car = 'jeep'
car == 'audi'
False

age = 18
age == 18
True

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
False
age_1 = 22
age_0 >= 21 and age_1 >= 21
True

requested_toppings = ['peppers', 'olives', 'pineapple']
'peppers' in requested_toppings
True
'pepperoni' in requested_toppings
False