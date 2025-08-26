def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice")
        return

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print(f"{a} + {b} = {add(a, b)}")
    elif choice == '2':
        print(f"{a} - {b} = {subtract(a, b)}")
    elif choice == '3':
        print(f"{a} * {b} = {multiply(a, b)}")
    elif choice == '4':
        try:
            result = divide(a, b)
            print(f"{a} / {b} = {result}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()