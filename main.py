# Simple Python calculator: adds two numbers entered by the user
def main():
    operation = ''
    print("Simple Addition/Multiplication Calculator")
    operation = input("Choose operation (+ for addition, * for multiplication): ")
    if operation  == '+':
        print("You chose addition.")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}")
    elif operation == '*':
        print("You chose multiplication.")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 * num2
        print(f"The product of {num1} and {num2} is {result}")
    else:
        print("Invalid operation. Please choose either + or *.")    

if __name__ == "__main__":
	main()
