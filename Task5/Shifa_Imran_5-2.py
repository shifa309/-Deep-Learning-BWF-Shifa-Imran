answer = 17
if answer != 42:
	print("That is not the correct answer. Please try again!")

# True test for string equality
if "hello" == "hello":
    print("Strings are equal")
else:
    print("Strings are not equal")
    
# False test for string equality
if "hello" == "world":
    print("Strings are equal")
else:
    print("Strings are not equal")
    
# True test for lower() function
if "HELLO".lower() == "hello":
    print("Strings are equal")
else:
    print("Strings are not equal")
    
# True test for numerical inequality
if 10 != 20:
    print("Numbers are not equal")
else:
    print("Numbers are equal")

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'audi':
		print(car.upper())
	else:
		print(car.lower())
