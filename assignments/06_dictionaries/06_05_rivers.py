rivers = {'nile': 'Egypt','amazon': 'Brazil','yenisey': 'Russia'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("Rivers included in the dictionary:")
for river in rivers.keys():
    print(river.title())

print("Countries included in the dictionary:")
for country in rivers.values():
    print(country.title())