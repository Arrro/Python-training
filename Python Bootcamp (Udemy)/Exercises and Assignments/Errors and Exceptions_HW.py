# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.

for i in ['a','b','c']:
    try:
        print(i**2)
    except TypeError:
        print("TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int")
    break

# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-1-c35f41ad7311> in <module>()
#       1 for i in ['a','b','c']:
# ----> 2     print(i**2)

# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

# Problem 2
# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("Division by zero is not allowed")

# ---------------------------------------------------------------------------
# ZeroDivisionError                         Traceback (most recent call last)
# <ipython-input-2-6f985c4c80dd> in <module>()
#       2 y = 0
#       3 
# ----> 4 z = x/y

# ZeroDivisionError: division by zero

# Problem 3
# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            num = int(input("Input and integer: "))
        except TypeError:
            print("An error occurred! Please try again!")
        else:
            num = num ** 2
            print(f"Thank you, your number squared is: {num}")
            break

ask()

# Input an integer: null
# An error occurred! Please try again!
# Input an integer: 2
# Thank you, your number squared is:  4
# Great Job!