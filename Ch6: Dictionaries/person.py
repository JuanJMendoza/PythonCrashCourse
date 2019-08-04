'''
Use a dictionary to store information about a person you know. Store their first name,
last name, age, and they city in which they live. You should have keys such as 
first_name, last_name, age, and city. Print each piece of information stored in your
dictionary.
'''
Me = {
    'full name': "Juan J. Mendoza",
    'school': "The University at Buffalo",
    'major': "Computer Science",
    'relationship status': "taken",
    'age': 26,
}

for data in Me:
    print(f"{data}: {Me[data]}")