polled = {
    'gerardo': 'matlab',
    'juan': 'javascript',
    'dan': 'python'
}

people = ['juan','edmund','dan','jacob','shawn','gerardo']

for peoplePolled in people:
    if peoplePolled in polled:
        print(f'\nThank you {peoplePolled.title()}, but we need people who haven\'t been polled yet.')
    else:
        print(f'''\nThank you {peoplePolled.title()}, for taking the survey with us, as compensation for your time '''
            ''' we'll send you a $15 gift card after you finish our survey.''')