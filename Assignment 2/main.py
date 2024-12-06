from calc import add, subtract, multiply, divide

def main():
       while True:
        operation = input("Enter an operation (add, subtract, multiply, divide): ").lower()
        
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")

            if operation == "add":
                result = add(num1, num2)

            elif operation == "subtract":   
                result = subtract(num1, num2)

            elif operation == "multiply":
                result = multiply(num1, num2)

            elif operation == "divide":
                result = divide(num1, num2)

            else:
                result = "Invalid operation."

            print("Result:", result)

            if input("Would you like to make another operation?  (yes/stop): ").lower() != "yes":
                break

