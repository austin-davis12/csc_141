pet1 = { 'animal_type': 'Cat','owner': 'Austin'}

pet2 = { 'animal_type': 'Dog', 'owner': 'Jackson'}

pet3 = {'animal_type': 'Parrot','owner': 'Ryan'}


pets = [pet1, pet2, pet3]

for pet in pets:
    print("\nHere is what I know about this pet:")
    print(f"Animal type: {pet['animal_type'].title()}")
    print(f"Owner: {pet['owner'].title()}")