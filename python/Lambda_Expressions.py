# Map Function - Apply a function to all items in an iterable object

def splicer(mystring):
    if len(mystring)%2==0:
        return 'EVEN'
    else:
        return mystring[0]

name = ["Eve", "Andy", "Sally"]

print(list(map(splicer, name)))