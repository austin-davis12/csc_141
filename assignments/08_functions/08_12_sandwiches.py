def make_sandwich(*toppings):
    print('\nThis sandwich was ordered:')
    for topping in toppings:
        print(f'- {topping}')

make_sandwich('Bacon')
make_sandwich('Pepperoni','Cheese')
make_sandwich('Bacon','Lettuce', 'Tomato')