def calculator():
    print("Simple Calculator")
    print("Available operators: +  -  *  /  %  **  //")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter operator: ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error: Division by zero"
        elif operator == '%':
            result = num1 % num2
        elif operator == '**':
            result = num1 ** num2
        elif operator == '//':
            if num2 != 0:
                result = num1 // num2
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operator!"

        return f"Result: {result}"
    except ValueError:
        return "Invalid input! Please enter numeric values."

# Run the calculator
print(calculator())

