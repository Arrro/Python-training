# Python Statements
# Tuple unpacking
mylist = [(1,2),(3,4),(5,6),(7,8)]
for a,b in mylist:
    print(a)
    print(b)

d = {'k1':1,'k2':2,'k3':3}
for key,value in d.items():
    print(value)

# While loops
x = 0
while x < 5:
    print(f'The current value of x i {x}')
    x += 1
else:
    print ("X IS NOT LESS THAN 5")

x = [1,2,3]
for item in x:
    # Comment
    pass
print('End of my script')
# Runs with the empty for loop and print statement

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)
# Prints Smmy

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        break
    print(letter)
# Prints S

# Useful operators
mylist = [1,2,3]
for num in range(3,10):
    print(num)

range(0,11,2) # Will return nothing as its a generator
list(range(0,11,2)) # Will return a list as its cast via the list

word = 'abcde'

for item in enumerate(word):
    print(item)

mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for item in zip(mylist1, mylist2):
    print(item)

2 in [1,2,3]
'a' in 'a world'
'mykey' in {'mykey':345}

from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist) # Shuffles the values

from random import randint
randint(0,100)

input('Enter a number here: ')

# List Comprehensions
mystring = 'hello'
mylist = [letter for letter in mystring] # Same as a for loop with the append function

mylist = [x for x in 'word']

mylist = [x for x in range(0,11) if x%2==0]

celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]

results = [x if x%2==0 else 'ODD' for x in range(0,11)]

mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]

# Section 5 assessment
# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word.startswith('s'):
        print(word)

# Use range() to print all the even numbers from 0 to 10.
for num in range(0,11):
    if num%2 == 0:
        print(num)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
divisList = [num for num in range(1,51) if num%3 == 0]

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2 == 0:
        print(word)

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".


# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'