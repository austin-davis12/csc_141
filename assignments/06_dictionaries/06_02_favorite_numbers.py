favorite_numbers = {'Jean Paul': 21, 'Brady': 7, 'Mike': 1, 'Kendall': 55, 'Jermaine': 8}

print(favorite_numbers['Jean Paul'])
print(favorite_numbers['Brady'])
print(favorite_numbers['Mike'])
print(favorite_numbers['Kendall'])
print(favorite_numbers['Jermaine'])

for name in favorite_numbers.keys():
    print(name.title())