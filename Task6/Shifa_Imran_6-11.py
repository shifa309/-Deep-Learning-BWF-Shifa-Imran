cities = {
    'new york': {'country': 'USA', 'population': '868638', 'fact': 'The Statue of Liberty is located in New York Harbor.'},
    'london': {'country': 'England', 'population': '881688', 'fact': 'London is home to the oldest underground system in the world.'},
    'tokyo': {'country': 'Japan', 'population': '13768638', 'fact': 'Tokyo has the busiest pedestrian crossing in the world.'}
}

for city, infor in cities.items():
    print("\nCity: " + city.title())
    print("\tCountry: " + infor['country'])
    print("\tPopulation: " + infor['population'])
    print("\tFact: " + infor['fact'])

