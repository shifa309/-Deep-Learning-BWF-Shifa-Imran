
count = ['China', 'Singapore', 'Pkistan', 'Newyork']
print("Countries:", count)

count.append("UK")
print("List after appending UK:", count)

count.insert(1, "Germany")
print("List after inserting Germany:", count)

count.remove("Singapore")
print("List after removing Singapore:", count)

pop = count.pop()
print("List after popping the last item " , count)

count.sort()
print("List after sorting alphabetically:", count)

count.reverse()
print("List after reversing the order:", count)

count.clear()
print("Empty list:", count)
