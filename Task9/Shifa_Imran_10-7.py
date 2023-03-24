while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 + num2
        print(f"The result is: {result}")
        
    except ValueError:
        print("Invalid input! Please enter a number.")
        
    #can also use else instead of finally
    finally:
        choice = input("Do you want to perform another addition? (1 for yes/2 for no) ")
        if choice == '2':
            break

