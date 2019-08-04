'''Exercise 6-7'''

people = {
    'juan': {
        'full name': "Juan J. Mendoza",
        'school': "The University at Buffalo",
        'major': "Computer Science",
        'relationship status': "taken",
        'age': 26,
    },
    'gerardo': {
        'full name': "Gerardo Chaca",
        'school': "SUNY Maritime",
        'major': "Mechanical Engineering",
        'relationship status': "married",
        'age': 26,
    },
    'moises': {
        'full name': "Moises Rivera",
        'school': "Brooklyn College",
        'major': "Psychology",
        'relationship status': "single",
        'age': 32,
    },
}

print('Information we have on our targets:')

for name, user_info in people.items():
    print('\nLoading...')
    print(f"{name}:")
    print(f"\tFull Name: {user_info['full name'].title()}")
    print(f"\tSchool: {user_info['school'].title()}")
    print(f"\tMajor: {user_info['major'].title()}")
    print(f"\tRelationship Status: {user_info['relationship status'].title()}")
    print(f"\tAge: {user_info['age']}")

