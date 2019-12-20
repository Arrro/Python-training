# Functions
def name_function(name='NAME'):
    '''
    DOCSTRING: Information about the function
    INPUT: No input ..
    OUTPUT: Hello ..
    '''
    return 'Hello '+name

result = name_function()

# Pig latin translator
def pig_latin(word):
    if word[0] in 'aeiou':
        return word + 'ay'
    else:
        return word[1:] + word[0] + 'ay'

# *args and **kwargs
def myfunc1(*args):
    return sum(args) * 0.05

def myfunc2(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choise is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

# Args returns a tuple while kwargs returns a dictionary
def myfunc3(*args, **kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))

# Lambda functions/ expressions
def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print(item)

def splicer(myString):
    if len(myString)%2 == 0:
        return 'EVEN'
    else:
        return myString[0]

names = ['Andy', 'Eve', 'Sally']
list(map(splicer,names))

def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]
for n in filter(check_even, mynums):
    print(n)

def squares(num): return num ** 2

# The above into the below
square = lambda num: num ** 2
list(map(lambda num: num**2, mynums))
list(filter(lambda num: num%2 == 0, mynums))