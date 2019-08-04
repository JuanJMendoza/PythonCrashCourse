'''
A Python dictionary can be used to model an actual dictionary. However, to avoid 
confusion, let's call it a glossary.

- Think of five programmnig words you've learned about in the previous chapters. 
Use these words as keys in your glossary, and store their meanings as values.

- Print each word and its meaning as neatly formatted output. You might print the
word followed by a colon and then its meaning, or print the word on one line and then
print its meaning indented on a second line. Use the newline character (\n) to insert a 
blank line between each word-meaning pair in your output.
'''

glossary = {
    'for-loops': '''A for-loop is a statement in programming that allows you to do '''
                '''something a number of times which is contingent on the range you '''
                '''specify.''',
    'comments': '''A comment information you put in your code that isn't ran by the '''
                '''the compiler and is used for describing your code.''',
    'strings': '''A string is a list of characters, but isn't nessecarily treated as '''
                '''as a list in many cases.''',
    'dictionary': "A dictionary is an object that holds \'items\' as key-value pairs.",
    'lists': "A list is an object used to hold any kind of element.",
}

print("List of Programming Words.\n")

for word in glossary:
    print(f"The definition of a {word} is: \n{glossary[word]}\n")