def city_country(city_name,city_country):
    #This program tells you a city and the country it is in 
    city_structure = f'"{city_name}, {city_country}"'
    return city_structure.title()

city_1 = city_country('Los Angeles','United States')
print(city_1)

city_2 = city_country('Venice','Italy')
print(city_2)

city_3 = city_country('Munich','Germany')
print(city_3)