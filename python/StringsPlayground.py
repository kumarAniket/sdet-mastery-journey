print('hello')
print("world")

print('this is also a string')
print("I'm going on a run")

print("hello world one")
print("hello world two")
print()
print('hello\nworld')
print('hello\tworld')

print(len("I am hungry"))
print()
print("------ Coding Challenge ------")
# Coding Challenge 2: Write code that prints out "Hello World"
print("Hello World")
print("Length >> {}".format(len("Hello World")))

print()
print("---------------------------------")
print("-- Indexing & Slicing Practice --")
print("---------------------------------")
myString = "Hello World"
print(myString[0])
print(myString[8])
print(myString[-2])
print(myString[-1])

print()
myString = "abcdefghijk"
print(myString[2:])
print(myString[:3])
print(myString[3:6])
print(myString[1:3])
print(myString[4:7])
print(myString[::-1])
print()
print("------ Indexing Coding Challenge ------")
# Coding Challenge 3: Write code that returns just the letter 'r' from "Hello World"
myString = "Hello World"
print(myString[-3])
print()
print("------ Slicing Coding Challenge ------")
# Coding Challenge 4: Use string slicing to grab the word 'ink' from inside 'tinker'
myString = "tinker"
print(myString[1:4])

print()
# String Properties & Methods
print("------ Immutability ------")
name = "Sam"
# name[0]="P"
last_letter=name[1:]
print('P'+last_letter)

x="Hello World"
x+= " it is beautiful outside"
print(x)

print('z'*10)

x='Hello World'
x = x.upper()
print(x)
print(x.lower())
print(x.split(" "))
print()
print("---------------------------------")
print("------- String Formatting -------")
print("---------------------------------")

# .format method
print("This is a string {}".format('INSERTED'))
print('The {2} {1} {0}'.format('fox','brown','quick'))
print('The {q} {b} {f} jumped over the wall'.format(q="quick",f="fox",b="brown"))
result=104.12345/777
print(result)

print()
print("The result was {r:1.5f}".format(r=result))

#f-strings
print()
name="Aniket"
print(f"Hello, his name is {name} with a result of {result:1.5f}")

# Coding Challenge 5: Write an expression using string formatting and return 'Python rules!'
print()
print("------ String Formatting Coding Challenge ------")
print('Python {}!'.format("rules"))
print('{p} rules!'.format(p="Python"))
print()
insertText = "rules!"
print(f'Python {insertText}')