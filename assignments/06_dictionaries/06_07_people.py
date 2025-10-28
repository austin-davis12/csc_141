Austin = {  'first_name': 'Austin', 'last_name': 'Davis','age': '18', 'city': 'West Grove'}

Jackson = { 'first_name': 'Jackson', 'last_name': 'Davis', 'age': '12', 'city': 'West Grove'}

Ryan = {'first_name': 'Ryan','last_name': 'Lauzon','age': '18','city': 'Landenburg'}


people = [Austin, Jackson, Ryan]


for person in people:
    print(f"\nName: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")