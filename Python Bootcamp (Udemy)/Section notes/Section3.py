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
myfile = open('myfile.txt')
contents = myfile.read()
myfile.seek(0) # returns the 'cursor' to the begininng 
myfile.readlines() # Returns them as an object
myfile.close()
with open ('myfile.txt') as my_new_file:
    contents = my_new_file.read()
with open ('myfile.txt', mode = 'w') as myfile:
    contents = myfile.write('blah\n')
    myfile.close()

### Objects and Data structures Assessment ###
# Write a brief description of all the following Object Types and Data Structures we've learned about:
# Numbers: a numeric integer, float, long or any other type of "number" and its respective type
# Strings: Any specified set of characters typically contained with ' or "
# lists: A structure that can contain any assortment of strings, variables and numbers in a way to be sorted or gone through
# Tuples: A Defined set of values in a row that are immutable
# Dictionaries: Key value pairs that are mutable and are able to hold other strucutres within them

### Numbers
# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
# Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25
numMatQ = 11**2 / 2.0 + 40 - .25

# Explain what the cell below will produce and why. Can you change it so the answer is correct?
2/3 # Produces 0
2.0/3.0 # Gives the full float value

# Answer these 3 questions without typing code. Then type code to check your answer.
#     What is the value of the expression 4 * (6 + 5)
        # 44
#     What is the value of the expression 4 * 6 + 5 
        # 29
#     What is the value of the expression 4 + 6 * 5
        # 34
# What is the *type* of the result of the expression 3 + 1.5 + 4?
    # Float
# What would you use to find a number’s square root, as well as its square? 
100 ** 0.5

### Strings
# Given the string 'hello' give an index command that returns 'e'. Use the code below:
s = 'hello'
# Print out 'e' using indexing
print(s[1])
# Reverse the string 'hello' using indexing:
s ='hello'
# Reverse the string using indexing
print(s[::-1])
# Given the string hello, give two methods of producing the letter 'o' using indexing.
s ='hello'
###
print(s[4])
print(s[-1])

### Lists
# Build this list [0,0,0] two separate ways.
list1 = [0,0,0]
list2 = [0]*3

# Reassign 'hello' in this nested list to say 'goodbye' item in this list:
l = [1,2,[3,4,'hello']]
l[2][2] = 'goodbye'
# Sort the list below:
l = [5,3,4,6,1]
l.sort()
sorted(l)
### Dictionaries
# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
# Grab 'hello'
d['simple_key']
d = {'k1':{'k2':'hello'}}
# Grab 'hello'
d['k1']['k2']
# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello
d['k1'][0]['nest_key'][1]
# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#Grab hello
d['k1'][2]['k2'][1]['tough'][2]
# Can you sort a dictionary? Why or why not?
    # Dictionaries are unsorted and can not be sorted

### Tuples
# What is the major difference between tuples and lists?
    # Tuples are immutable and lists are mutable
# How do you create a tuple?
myTup = (1,2,3)

### Sets 
# What is unique about a set?
    # Sets can be ordered and sorted, they can also contain mutiple value types
# Use a set to find the unique values of the list below:
l = [1,2,2,33,4,4,11,22,3,3,2]
set(l)

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
False
# Answer before running cell
3 <= 2
False
# Answer before running cell
3 == 2.0
False
# Answer before running cell
3.0 == 3
True
# Answer before running cell
4**0.5 != 2
False

# Final Question: What is the boolean output of the cell block below?
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

#True or False?
l_one[2][0] >= l_two[2]['k1']
    # 3 >= 4 is False