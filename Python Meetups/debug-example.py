# What is debugging and when/ why would you use it?
# Great for getting down into the roots of a problem
# Typical way of debugging would be to use print to output a simple "test" in a loop or a function
# While useful, its archaic and doesnt really diagnose the problem, even if it does resolve a specific issue

# How do you debug in Python?
# You can use and IDE's/ editors built in debugging tool
# You can use Pythons debugging module

# Python pdb
# https://codeburst.io/how-i-use-python-debugger-to-fix-code-279f11f75866
# https://docs.python.org/3.7/library/pdb.html
# https://docs.python.org/3.7/library/pdb.html#debugger-commands

# run python -m pdb debug-example.py to trigger the built in debugger or you can place pdb.set_trace() at a spot to begin a debug session in that frame
# While powerful and useful for verifying and stepping through the source line level and inspection of stack frame it is rather hard to use
import pdb

test = ["Hello", "World", "test"]

for words in test:
    if (words != "test"):
        print(words)

# pdb.set_trace(); This will prompt the CL with some options for iterarting through a stack

# Built in debug tool
    # VScode has a built in debugging tool as does most IDE's like PyCharm
    # Key words:
        # Breakpoint - Intentional stop or pause placed
        # Useful for wanting to stop and ensure the proper values are being entered into a variable or a loop is iterating properly
        # Step Over - Will continue a program/ function or whatever frame you are currently in by one step
        # Step Into - If another function is present it will step into the next procedure, if not function is present it will act as a Step Over
        # Continue - Will tell the debugger to go forward until the next breakpoint is hit
        # Step Out - An action that will return the debugger to the current function being called
        # Useful if wondering where something is being called from
    # Debug console
        # Useful way of determine what a value holds
    # Logpoint
        # Used for when you wish for the debugger to log a message to the console instaead of "breaking" the debugger. Really useful for adding errors to console
    # Conditional Breakpoints - https://code.visualstudio.com/docs/editor/debugging#_conditional-breakpoints
    # Watch panel - It will aid in watching values change during execution of a program / script

test2 = {'1': "not me", '2': "Not me Either", 3: "Me!"}

for key in test2:
    if (key == '3'):
        print(test2['3'])
