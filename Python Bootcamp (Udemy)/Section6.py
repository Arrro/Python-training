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