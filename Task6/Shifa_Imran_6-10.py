favorite_numbers = {
    "Shifa": [5, 7, 9],
    "Mashal": [10, 23],
    "Haleema": [76],
    "Ayesha": [100, 55],
    "Bisma": [43, 33, 22]
}
for name, numbers in favorite_numbers.items():
    print(name + "'s favorite numbers are:")
    for number in numbers:
        print(": " + str(number))
    print()

