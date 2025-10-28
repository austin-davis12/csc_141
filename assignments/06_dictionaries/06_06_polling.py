favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}


people = ['jen', 'sarah', 'edward', 'phil', 'jim']


for person in people:
    if person in favorite_languages:
        print(f"Thanks {person.title()}, for taking the poll!")
    else:
        print(f"{person.title()}, please take our favorite languages poll!")