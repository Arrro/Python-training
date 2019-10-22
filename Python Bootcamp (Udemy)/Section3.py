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
