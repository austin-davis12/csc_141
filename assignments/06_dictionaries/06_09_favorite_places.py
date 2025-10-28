favorite_places = {'Austin': ['Philadelphia'],'Jackson': ['West Chester'],'Ryan': ['Florida']}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite place:")
    for place in places:
        print(f"- {place}")