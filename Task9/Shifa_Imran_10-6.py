while True:
    try:
        n1 = int(input("Enter the 1st number: "))
        n2 = int(input("Enter the 2nd number: "))
        result = n1 + n2
        print(f"The result is: {result}")
        break
    except ValueError:
        print("Invalid input! Please enter a number.")
