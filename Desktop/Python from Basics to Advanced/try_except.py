try:
    num = int(input("Enter a number: "))
    print("10 divided by your number:", 10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
