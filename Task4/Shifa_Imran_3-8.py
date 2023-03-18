places = ['China', 'Singapore', 'Pkistan', 'Newyork']

#original order
print("\nOriginal order:")
print(places)

#alphabetical order --- sorted()
print("\nAlphabetic order:")
print(sorted(places))

# list to show it's still in its original order
print("\nOriginal order (again):")
print(places)

# list in reverse alphabetical order using sorted()
print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))

# Print the list to show it's still in its original order
print("\nOriginal order (again):")
print(places)

# Change the order of the list using reverse()
places.reverse()

# Print the list to show it has been reversed
print("\nReversed order:")
print(places)

# Change the order of the list again using reverse()
places.reverse()

# show it's back to its original order
print("\nOriginal order (again):")
print(places)

# Change the order of the list using sort()
places.sort()

#show it's in alphabetical order
print("\nAlphabetical order:")
print(places)

# Change the order of the list using sort() 
places.sort(reverse=True)

# show it's in reverse alphabetical order
print("\nReverse alphabetical order:")
print(places)
