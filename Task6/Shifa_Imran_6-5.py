rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Mississippi ': 'United States',
	'Ganges ' : 'India'
}

for river, country in rivers.items():
    print("The " + river.title() + " runs through" + country.title())

print("\nRivers Names")
for river in rivers.keys():
    print(river.title())

print("\nCountries Names")
for country in rivers.values():
    print(country.title())
