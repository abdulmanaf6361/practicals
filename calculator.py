# create a simple python calculator that can add, subtract, multiply and divide two numbers
# print the result to the user without functions
print("Welcome to the simple calculator!")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("The sum of " + str(num1) + " and " + str(num2) + " is: " + str(num1 + num2))
print("The difference of " + str(num1) + " and " + str(num2) + " is: " + str(num1 - num2))
print("The product of " + str(num1) + " and " + str(num2) + " is: " + str(num1 * num2))
if num2 != 0:
    print("The quotient of " + str(num1) + " and " + str(num2) + " is: " + str(num1 / num2))
else:
    print("Cannot divide by zero!")