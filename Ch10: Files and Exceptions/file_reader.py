'''READING ENTIRE FILE'''
'''
The open() function need one argument: the name of the file you want to open. Python looks for this file in the directory where the program that's currently running, 
so python looks for pi_digits.txt in the directory where file_reader.py is stored. The open() function returns an object representing the file.
'''
with open('pi_digits.txt') as file_object:
    '''The keyword 'with' closes the file once access to it is no longer needed.'''

    '''Notice how we call open() in this program but never close(). You could open and close the file by calling open() and close(), but if a bug in your program prevents
        the close() method from being executed, the file may never close.'''

    contents = file_object.read() #We use the read() method to read the ENTIRE contents of the file and store it as one long string in contents.
# print(contents) #When we print the value of contents, we get the ENTIRE text file back.

'''READING FILE LINE BY LINE'''
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        # print(line.rstrip())
        pass

'''MAKING A LIST OF LINES FROM A FILE'''
with open(filename) as file_object:
    '''readlines() method takes each line from the file and stores it in a list.'''
    lines = file_object.readlines() 

for line in lines:
    # print(line.rstrip())
    pass
