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