# Format method
print('This is a {2} and not a {0} or {1}'.format('quiz','paper','test'))
result = 100/777
print("The result was {r:1.3f}".format(r=result))
name = "Jose"
print(f'Hello, {name}')
print("Hello {0}".format(name))

# Dictionaries
d = {'k1':123, 'k2':[0,1,2,3], 'k3':{'insideKey':100}}
d['k2'][2]
d['k3']['insideKey']
print(d)
print(d.values())

# Tuples
t = ('a','a','b')
print(t.count('a'))
print(t.index('a'))

# File I/O

### Objects and Data structures Assessment ###
# Write a brief description of all the following Object Types and Data Structures we've learned about: 

# Numbers:
#
# Strings:
#
# lists:
# 
# Tuples:
# 
# Dictionaries:
# 

### Numbers
# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
# Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

# Explain what the cell below will produce and why. Can you change it so the answer is correct?

2/3

# Answer these 3 questions without typing code. Then type code to check your answer.
# 
#     What is the value of the expression 4 * (6 + 5)
#     
#     What is the value of the expression 4 * 6 + 5 
#     
#     What is the value of the expression 4 + 6 * 5 

# What is the *type* of the result of the expression 3 + 1.5 + 4?

# What would you use to find a number’s square root, as well as its square? 

### Strings

# Given the string 'hello' give an index command that returns 'e'. Use the code below:

s = 'hello'
# Print out 'e' using indexing

# Reverse the string 'hello' using indexing:

s ='hello'

# Reverse the string using indexing


# Given the string hello, give two methods of producing the letter 'o' using indexing.

s ='hello'



### Lists

# Build this list [0,0,0] two separate ways.

# Reassign 'hello' in this nested list to say 'goodbye' item in this list:

l = [1,2,[3,4,'hello']]

# Sort the list below:

l = [5,3,4,6,1]

### Dictionaries

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}
# Grab 'hello'

d = {'k1':{'k2':'hello'}}
# Grab 'hello'

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}


# Can you sort a dictionary? Why or why not?

### Tuples

# What is the major difference between tuples and lists?

# How do you create a tuple?

### Sets 

# What is unique about a set?

# Use a set to find the unique values of the list below:

l = [1,2,2,33,4,4,11,22,3,3,2]

# ## Booleans
# For the following quiz questions, we will get a preview of comparison operators:

# If the values of two operands are equal, then the condition becomes true.
# (a == b) is not true.

# If values of two operands are not equal, then condition becomes true.
# <>
# If values of two operands are not equal, then condition becomes true.
#  (a <> b) is true. This is similar to != operator.

# >
# If the value of left operand is greater than the value of right operand, then condition becomes true.
#  (a > b) is not true.

# >
# If the value of left operand is less than the value of right operand, then condition becomes true.
#  (a < b) is true.

# >=
# If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.
#  (a >= b) is not true. 

# <=
# If the value of left operand is less than or equal to the value of right operand, then condition becomes true.
#  (a <= b) is true. 

# What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# Answer before running cell
2 > 3

# Answer before running cell
3 <= 2

# Answer before running cell
3 == 2.0

# Answer before running cell
3.0 == 3

# Answer before running cell
4**0.5 != 2

# Final Question: What is the boolean output of the cell block below?

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

#True or False?
l_one[2][0] >= l_two[2]['k1']