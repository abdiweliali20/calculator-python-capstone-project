import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def square_root(x):
    if x < 0:
        return "Error! Cannot calculate square root of a negative number."
    else:
        return math.sqrt(x)

def exponentiate(x, y):
    return x ** y

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def calculator():
    print("Welcome to the Scientific Calculator!")
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Exponentiation")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("0. Exit")

    while True:
        choice = input("Enter operation (0-9): ")

        if choice == '0':
            print("Exiting calculator.")
            break

        if choice in ('1', '2', '3', '4', '6'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        elif choice in ('5', '7', '8', '9'):
            num = float(input("Enter number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", square_root(num))
        elif choice == '6':
            print("Result:", exponentiate(num1, num2))
        elif choice == '7':
            print("Result:", sin(num))
        elif choice == '8':
            print("Result:", cos(num))
        elif choice == '9':
            print("Result:", tan(num))
        else:
            print("Invalid input! Please enter a number between 0 and 9.")

if __name__ == "__main__":
    calculator()
