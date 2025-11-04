sandwich_orders = ['Italian', 'Pastrami','Turkey', 'Pastrami','Pepperoni','Ham','Pastrami','Chicken']
finished_sandwiches = []

print('The deli has run out of pastrami')
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
print(sandwich_orders)

while sandwich_orders:
    sandwiches = sandwich_orders.pop()

    print(f'Your {sandwiches} samdwich is ready!')
    finished_sandwiches.append(sandwiches)

print(f'\nThe following sandwiches have been made:')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)