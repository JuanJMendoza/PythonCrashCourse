'''
One common issue when working with files is handling missing files. The file you're looking for might be in a different location, the filename may be mispelled, or the file may not exist at all. 
You can handle all these situations in a straightforward way with a try-except block.
'''

def count_words(filename):
    """Count the approximate number of words in the file."""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
        # If we wanted our program to fail silently, we'd leave a 'pass' inside the except block on a FileNotFoundError so it does nothing and continues.
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
    

filenames = ['alice.txt','siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    count_words(filename)