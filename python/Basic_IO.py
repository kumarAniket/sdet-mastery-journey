myfile = open('Basic_IO_File.txt')
myfile.read()
myfile.seek(0)
print(myfile.readlines())
myfile.close()
print()
print("Using the with command:")
with open('/Users/asingh/Downloads/test.txt') as new_file:
    print(new_file.read())
print()
# Modes for files
# r - Only read, w - Only write (overwrites file / creates new file), a - Append (Adds to the end of a file), r+ - Reading and writing, w+ - Writing and reading

# Mode: r
print("-------- Mode: r --------")
with open('/Users/asingh/Downloads/test.txt', mode='r') as new_file:
    print(new_file.readlines())
# Mode: w
print("-------- Mode: w --------")
with open('/Users/asingh/Downloads/test.txt',mode='w') as new_file:
    new_file.write('Updated lines\nLine No.1\nLine No.2\nLine No.3')
    print('Existing file updated')
with open('/Users/asingh/Downloads/codeFile.txt',mode='w') as newFile:
    newFile.write("File created from code")
    print("New file created")
# Mode: a
print("-------- Mode: a --------")
with open('/Users/asingh/Downloads/codeFile.txt',mode='a') as appendFile:
    appendFile.write("\nLast line added as part of append mode")
    print("Line appended")

with open('/Users/asingh/Downloads/codeFile.txt',mode='r') as readFileAppended:
    print(readFileAppended.readlines())

# Mode:r+
print("-------- Mode: r+ --------")
with open('/Users/asingh/Downloads/codeFile.txt',mode='r+') as readWriteFile:
    readWriteFile.write("New line as part of r+ mode")
with open('/Users/asingh/Downloads/codeFile.txt',mode='r') as updatedFile:
    print(updatedFile.readlines())

# Mode:w+
print("-------- Mode: w+ --------")
with open('/Users/asingh/Downloads/codeFileNew.txt',mode='w+') as writeReadFile:
    writeReadFile.write("Line added as part of w+ mode")
    print("Line added")

with open('/Users/asingh/Downloads/codeFileNew.txt',mode='r') as writeReadFile:
    print(writeReadFile.readlines())



# Coding Challenge 9: Open a file, write Hello World to it and then close the file
print()
print("------ File I/O Coding Challenge ------")
newFile = open('test.txt',mode='w')
newFile.write('Hello World')
newFile.close()
