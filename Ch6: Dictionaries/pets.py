pets = {
    'franklyn': {
        'name': 'franklyn',
        'type': "tutle",
        'owner': "juan",
    },
    'joey': {
        'name': 'joey',
        'type': "cat",
        'owner': "erika",
    },
    'suco': {
        'name': 'suco',
        'type': "dog",
        'owner': "gerardo",
    }
}

print("\nMiscellaneous Information.")

for name, info in pets.items():
    print(f"\n\tThe animal's name is {info['name'].title()}, its type is "
        f"{info['type'].title()}, and the owner's name is {info['owner'].title()}.")