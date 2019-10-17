'''WRITING TO AN EMPTY FILE'''
'''To write text to a file, you need to call open() with a second argument telling Python that you want to write to the file.'''
filename = 'programming.txt'

'''The first argument is still the name of the file we want to open. The second argument, 'w', tells Python that we want to open the file in '[w]rite mode'.'''
'''You can also open a file in read mode ('r'), write mode ('w'), append mode('a'), or a mode that allows you to read and write ('r+').'''
'''If you omit the mode argument, Python opens the file in read-only mode by defualt.'''
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")