# Simple Calculator Application

def show_menu():
    print("\n--- Simple Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed!"


def main():
    while True:
        show_menu()
        choice = input("Choose an operation (1-5): ")

        if choice == "5":
            print("Exiting the Calculator. Goodbye!")
            break

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == "1":
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == "2":
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == "3":
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == "4":
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
