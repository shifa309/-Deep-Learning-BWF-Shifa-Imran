x = ["hello", "world", "how", "are", "you"]

#returns it as an enumerate object but list is used to write in the form of list
y1 = enumerate(x)
print (list(y1))

#The enumerate() function adds a counter as the key of the enumerate object.
y2 = enumerate(x,2)
  print (list(y2))
