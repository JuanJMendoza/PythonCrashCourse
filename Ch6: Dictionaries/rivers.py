'''
Make a dictionary containing three major rivers and country each river runs through.
One key-value pair might be 'nile': 'egypt'.
- Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
- Use a loop to print the name of each river included in the dictionary.
- Use a loop to print the name of each counrty included in the dictionary.
'''
rivers = {
    'nile': 'egypt',
    'missisippi' : 'united states',
    'danube': 'germany',
}

for river, country in rivers.items():
    print(f'The {river.title()} river flows through {country.title()}. Unbelivable!!')