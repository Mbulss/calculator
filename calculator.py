def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero."
    return x / y

def power(x, y):
    return x ** y

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'power' for exponentiation")
    print("Enter 'quit' to end the program")

    user_choice = input(": ")

    if user_choice == "quit":
        break
    elif user_choice in ("add", "subtract", "multiply", "divide", "power"):
        num1 = get_number_input("Enter first number: ")
        num2 = get_number_input("Enter second number: ")

        if user_choice == "add":
            result = add(num1, num2)
        elif user_choice == "subtract":
            result = subtract(num1, num2)
        elif user_choice == "multiply":
            result = multiply(num1, num2)
        elif user_choice == "divide":
            result = divide(num1, num2)
        elif user_choice == "power":
            result = power(num1, num2)

        print("Result:", result)
    else:
        print("Invalid input. Please enter a valid operation.")
