cubes = []

for i in range(1, 11):
    cube = i**3
    cubes.append(cube)

print(cubes)

print("\nThe first three items: ", cubes[:3])
print("Three items from the middle: ", cubes[3:6])
print("The last three items: ", cubes[-3:])

