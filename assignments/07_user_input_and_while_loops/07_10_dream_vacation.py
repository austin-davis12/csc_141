places = {}
polling_active = True

while polling_active:
    name = input('What is your name?')
    place = input('\nIf you could visit one place in the world where would it be? ')
    
    places[name] = place
    
    repeat = input('Would anyone else like to answer the poll? ')
    if repeat == 'no':
        polling_active = False
        
print('\n   Poll Results   ')
for name, place in places.items():
    print(f'{name} would like to visit {place}')