
guests = ['Imran', 'Ali', 'Ayesha' , 'Haleema']

print("Sorry, I can only invite two people for dinner.")

not_guest1 = guests.pop()
print("Sorry " + not_guest1.title() + " I can't invite you to dinner anymore.")
not_guest2 = guests.pop()
print("Sorry " + not_guest2.title() + " I can't invite you to dinner anymore.")

print(guests[0].title() + " and " + guests[1].title() + " you're still invited to dinner!")

del guests[:]
#will give an error as accessing when list is empty
print(guests[-1])
