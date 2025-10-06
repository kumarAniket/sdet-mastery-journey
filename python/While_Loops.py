x = 50
while x<5:
    print(f"The current value of x is {x}")
    x=x+1
else:
    print("x is not less than 5")


# Keywords
# break, continue, pass

# pass keyword
x = [1,2,3]
for item in x:
    pass
print('end of my script')

# continue keyword
mystring = "Sammy"
for letter in mystring:
    if letter == 'a':
        break
    print(letter)
print()
# break keyword
x=0
while x <5:
    print(x)
    if x==2:
        break
    x+=1