student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

A = {1, 7, 8}
B = {0, 2, 9, 7, 1}

print("A: " , A)
print("B: " , B)

# perform union operation -- | 
print('Union using |:', A | B)

# perform union operation -- union()
print('Union using union():', A.union(B)) 

# perform intersection operation -- &
print('Intersection using &:', A & B)

# perform intersection operation -- intersection()
print('Intersection using intersection():', A.intersection(B)) 

# perform difference operation -- &
print('Difference using &:', A - B)

# perform difference operation -- difference()
print('Difference using difference():', A.difference(B)) 

# perform difference operation -- &
print('Difference using &:', B - A)

# perform difference operation -- difference()
print('Difference using difference():', B.difference(A)) 

# perform symmetric difference operation -- &
print('Symmetric difference using ^:', A ^ B)

# perform symmetric difference using symmetric_difference()
print('using symmetric_difference():', A.symmetric_difference(B))


#Making Data unique with sets
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)                  #{2, 4, 6, 8} 

#Here, we can see there are no duplicate items in the set 
as a set cannot contain duplicates.
