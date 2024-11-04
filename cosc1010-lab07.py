# Ethan Hall
# UWYO COSC 1010
# 10.28.2024
# Lab 07
# Lab Section: 
# Sources, people worked with, help given to: 
# your
# comments
# here


# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered

factorial = 1
userInput = True 
upperBound = 0

while(True):
    upperBound = input("Upper bound: ") 
    userInput = upperBound.isdigit()
    if (userInput):
        userInput = True
        break
    else:
        print("This is an invalid number. Please choose a positive integer.")
    break 

for i in range(1, int(upperBound) + 1):
            factorial *= i

print(f"The result of the factorial based on the bound {upperBound} is {factorial}")

print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
# To do so you can use the methods `.isdigit()` or `.isnumeric()`
# This will return true if every digit in your string is a numerical character
# However, that means a string such as `-1` would return false, even though your program should accept negative values
# This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
# If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
# I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 
num_sum = 0

while (True):
    userInput = input("Enter integers to sum or type 'exit' to leave: ")
    if userInput.isdigit(): 
        num_sum += int(userInput)
        
        break
    elif userInput[0] == "-" and userInput[1:] .isdigit(): 
        num_sum -= int(userInput[1:])
        break
    elif userInput == 'exit':
        break 
    else:
        print("error. invalid input.")
        
    
        
print(f"Your final sum is {num_sum}")


print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 

def is_positive_integer(value):
    if value.isdigit() and int(value) > 0:
        return True
    return False

def calculate(expression):
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else 'undefined',
        '%': lambda x, y: x % y
    }

    for operator in operators.keys():
        if operator in expression:
            operand1, operand2 = map(str.strip, expression.split(operator, 1))
            break
    else:
        return "Invalid operation"

    while not is_positive_integer(operand1) or not is_positive_integer(operand2):
        return "Invalid input. Please enter positive integers."

    operand1 = int(operand1)
    operand2 = int(operand2)

    return operators[operator](operand1, operand2)

def main():
    while True:
        user_input = input("Enter your calculation (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the calculator.")
            break
        result = calculate(user_input)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
